import os
from transformers import T5Tokenizer, T5ForConditionalGeneration, MarianMTModel, MarianTokenizer, AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import json

script_dir = os.path.dirname(__file__)

max_token_length = 256

with open(os.path.join(script_dir, "dev.json")) as user_file:
    file_contents = user_file.read()

# print(file_contents)

parsed_json = json.loads(file_contents)

model_name = "t5-small"

tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# task_prefix = "convert to SQL"
# use different length sentences to test batching

print("input encoding started")

input_ids = tokenizer(
    [json_obj['question'] for json_obj in parsed_json][5:],
    padding="longest",
    max_length=max_token_length,
    truncation=True,
    return_tensors="pt"
).input_ids

print("input encoded")
print(input_ids[0])

print("output encoding started")

labels = tokenizer(
    [json_obj['query'] for json_obj in parsed_json][5:],
    padding="longest",
    max_length=max_token_length,
    truncation=True,
    return_tensors="pt"
).input_ids

print("output encoded")
print(labels[0])

print("training started")
# the forward function automatically creates the correct decoder_input_ids
loss = model(input_ids=input_ids, labels=labels).loss
loss.item()
print("training ended")

inputs = tokenizer(
    ['What is the total number of clients in the database?'],
    padding="longest",
    max_length=max_token_length,
    truncation=True,
    return_tensors="pt"
)

output_sequences = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    do_sample=False,  # disable sampling to test if batching affects output
)

print(tokenizer.batch_decode(output_sequences, skip_special_tokens=True))
