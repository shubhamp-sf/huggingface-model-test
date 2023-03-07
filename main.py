from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("tscholak/cxmefzzi")

model = AutoModelForSeq2SeqLM.from_pretrained("tscholak/cxmefzzi")

promptInput = "How many singers do we have? | concert_singer | stadium : stadium_id, location, name, capacity, highest, lowest, average | singer : singer_id, name, country, song_name, song_release_year, age, is_male | concert : concert_id, concert_name, theme, stadium_id, year | singer_in_concert : concert_id, singer_id"

response = pipeline('text2text-generation', model=model,
                    tokenizer=tokenizer)(promptInput)

print(response)
