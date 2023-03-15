from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("tscholak/3vnuv1vf")

model = AutoModelForSeq2SeqLM.from_pretrained("tscholak/3vnuv1vf")

promptInput = [
    "Show me all hotels where the client with id 987 has made reservations with a rating of 4 or higher. | hoteldb | hotel : id, name, type | reservation : id, type, clientId, hotelId, rating, checkInDate, checkOutDate | client : id, name, username, address, telephone, age",
]

# prompt | database | table : col1, col2, col3
response = pipeline('text2text-generation', model=model,
                    tokenizer=tokenizer)(promptInput)

print(response)
