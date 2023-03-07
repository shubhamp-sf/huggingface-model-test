from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("tscholak/cxmefzzi")

model = AutoModelForSeq2SeqLM.from_pretrained("tscholak/cxmefzzi")

promptInput = "what is the price of Anniseed Syrup? | mystore | products : id, name, price, unit"
response = pipeline('text2text-generation', model=model,
                    tokenizer=tokenizer)(promptInput)

print(response)
