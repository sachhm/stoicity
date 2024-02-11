"""
quote_reader.py

read quotes from quotes.json
"""
import json, random

quotes_file = "data/quotes.json"

with open(quotes_file, "r") as file:
    data = json.load(file)
    quotes = data["quotes"]

    all_quotes = []

    for quote in quotes:
        text = quote["text"]
        author = quote["author"]
        quote_data = {"text": text, "author": author}
        all_quotes.append(quote_data)

def get_random_quote():
    rand_int = random.randint(0, len(all_quotes))
    return all_quotes[rand_int]

print(get_random_quote())