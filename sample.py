from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

promptInput = "we love sourcefuse"

response = pipeline('sentiment-analysis')(promptInput)

print(response)
