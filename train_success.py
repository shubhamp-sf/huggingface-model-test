from transformers import AdamW
from transformers import EncoderDecoderModel, BertTokenizer, EncoderDecoderConfig
import torch
import pandas as pd

from transformers import EncoderDecoderModel
from torch.utils.data import Dataset

import json

with open('/Users/harshad.kadam/Downloads/spider/dev.json') as user_file:
    dev_contents = user_file.read()
dev_json = json.loads(dev_contents)
print(dev_json[0])

with open('/Users/harshad.kadam/Downloads/spider/train_spider.json') as user_file:
    train_contents = user_file.read()
train_json = json.loads(train_contents)
print(train_json[0])


class Text2SqlDataset(Dataset):
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def __len__(self):
        return len(self.inputs["input_ids"])

    def __getitem__(self, index):
        return {
            "input_ids": self.inputs["input_ids"][index],
            "attention_mask": self.inputs["attention_mask"][index],
            "decoder_input_ids": self.outputs["input_ids"][index][:-1],
            "decoder_attention_mask": self.outputs["attention_mask"][index][:-1],
            "labels": self.outputs["input_ids"][index][1:]
        }


class EncoderDecoderTrainer:
    def __init__(self, model, args, train_dataset, eval_dataset, data_collator):
        print("***************")
        print(args)
        print("***************")
        self.model = model
        self.args = args
        self.train_dataset = train_dataset
        self.eval_dataset = eval_dataset
        self.data_collator = data_collator
        self.optimizer = AdamW(self.model.parameters(),
                               lr=args['learning_rate'])
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            self.optimizer, mode='min', factor=0.1, patience=3, verbose=True)

    def save_model(self, output_dir, tokenizer):
        self.model.save_pretrained(f"{output_dir}/text2Sql")
        tokenizer.save_pretrained(f"{output_dir}/text2Sql")

    def train(self):
        train_loader = torch.utils.data.DataLoader(
            self.train_dataset,
            batch_size=self.args['per_device_train_batch_size'],
            collate_fn=self.data_collator,
            shuffle=True
        )

        eval_loader = torch.utils.data.DataLoader(
            self.eval_dataset,
            batch_size=self.args['per_device_eval_batch_size'],
            collate_fn=self.data_collator,
            shuffle=False
        )
        print("********** training started ************")

        for epoch in range(self.args['num_train_epochs']):
            print(f"********** {epoch} started ************")
            self.model.train()
            total_loss = 0

            for step, batch in enumerate(train_loader):
                print(f"********** {epoch} started - {step} ************")
                inputs = {k: v.to(self.args['device'])
                          for k, v in batch.items() if k != "labels"}
                labels = batch["labels"].to(self.args['device'])

                outputs = self.model(**inputs, labels=labels)
                loss = outputs.loss
                total_loss += loss.item()

                loss.backward()
                torch.nn.utils.clip_grad_norm_(
                    self.model.parameters(), self.args['max_grad_norm'])
                self.optimizer.step()
                self.scheduler.step(loss)
                self.optimizer.zero_grad()

                if step % self.args['logging_steps'] == 0:
                    print(f"Epoch {epoch}, step {step}, loss {loss.item()}")

            print(f"********** {epoch} ended ************")
            avg_train_loss = total_loss / len(train_loader)
            print(f"Epoch {epoch}, average training loss {avg_train_loss}")

            self.model.eval()
            total_eval_loss = 0

            print(f"********** {epoch} eval started ************")
            # import pdb; pdb.set_trace()
            print(eval_loader)
            for step, batch in enumerate(eval_loader):
                print(f"********** {epoch} started - {step} ************")
                with torch.no_grad():
                    inputs = {k: v.to(self.args['device'])
                              for k, v in batch.items() if k != "labels"}
                    labels = batch["labels"].to(self.args['device'])

                    outputs = self.model(**inputs, labels=labels)
                    loss = outputs.loss
                    total_eval_loss += loss.item()

            avg_eval_loss = total_eval_loss / len(eval_loader)
            print(f"Epoch {epoch}, average evaluation loss {avg_eval_loss}")


# Load the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)

# Load the dataset
# replace with your own dataset
train_data = {"input": [data['question'] for data in train_json]
              [:200], "output": [data['query'] for data in train_json]}
# replace with your own dataset
valid_data = {"input": [data['question'] for data in train_json]
              [:100], "output": [data['query'] for data in dev_json]}

print("********************************")
print(train_data["input"][0], train_data["output"][0])
print("********************************")
print(valid_data["input"][0], valid_data["output"][0])
print("********************************")
# Tokenize the input and output sequences
train_inputs = tokenizer(
    train_data["input"],
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors="pt")
train_outputs = tokenizer(
    train_data["output"],
    padding=True,
    truncation=True,
    max_length=64,
    return_tensors="pt")
valid_inputs = tokenizer(
    valid_data["input"],
    padding=True,
    truncation=True,
    max_length=128,
    return_tensors="pt")
valid_outputs = tokenizer(
    valid_data["output"],
    padding=True,
    truncation=True,
    max_length=64,
    return_tensors="pt")
print("********************************")
print(train_inputs["input_ids"], train_outputs["input_ids"])
print("********************************")
# Initialize the model
model = EncoderDecoderModel.from_encoder_decoder_pretrained(
    model_name, model_name)

# Set the special tokens for the input and output sequences
model.config.decoder_start_token_id = tokenizer.cls_token_id
model.config.eos_token_id = tokenizer.sep_token_id
model.config.pad_token_id = tokenizer.pad_token_id

# Define the training parameters
training_args = {
    "learning_rate": 1e-4,
    "num_train_epochs": 1,
    "max_seq_length": 512,
    "per_device_train_batch_size": 256,
    "per_device_eval_batch_size": 256,
    "save_steps": 1000,
    "output_dir": "text_to_sql_model",
    "overwrite_output_dir": True,
    "logging_dir": "text_to_sql_logs",
    "logging_steps": 100,
    "eval_steps": 1000,
    "save_total_limit": 1,
    "device": torch.device("cpu"),
    "max_grad_norm": 1.0
}

# Define the data collator for padding the input and output sequences


def collate_fn(batch):
    input_ids = [item["input_ids"] for item in batch]
    attention_mask = [item["attention_mask"] for item in batch]
    decoder_input_ids = [item["input_ids"][:-1] for item in batch]
    decoder_attention_mask = [item["attention_mask"][:-1] for item in batch]
    labels = [item["input_ids"][1:] for item in batch]
    return {
        "input_ids": torch.stack(input_ids),
        "attention_mask": torch.stack(attention_mask),
        "decoder_input_ids": torch.stack(decoder_input_ids),
        "decoder_attention_mask": torch.stack(decoder_attention_mask),
        "labels": torch.stack(labels)
    }


# Initialize the trainer
trainer = EncoderDecoderTrainer(
    model=model,
    args=training_args,
    train_dataset=Text2SqlDataset(train_inputs, train_outputs),
    eval_dataset=Text2SqlDataset(valid_inputs, valid_outputs),
    data_collator=collate_fn
)

# Train the model
trainer.train()

print("---------------------")
print("training completed")

# Save the model
trainer.save_model("text_to_sql_model", tokenizer)
