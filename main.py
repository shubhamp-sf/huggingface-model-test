from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("tscholak/cxmefzzi")

model = AutoModelForSeq2SeqLM.from_pretrained(
    "tscholak/cxmefzzi")  # takes 1min 25 seconds to load

promptInput = [
    "what is the price of Anniseed Syrup? | mystore | products : id, name, price, unit"]

# prompt | database | table : col1, col2, col3
text2sql = pipeline('text2text-generation', model=model,
                    tokenizer=tokenizer)  # took 34 seconds

response = text2sql(promptInput)
print(response)
