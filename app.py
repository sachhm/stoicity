"""
app.py

main web app
"""

from flask import Flask
from flask import render_template

import quote_reader

app = Flask(__name__)


@app.route('/')
def home():
    quote = quote_reader.get_random_quote()
    text=quote['text'].capitalize()
    author=quote['author']
    print(quote) # debug statement 
    return render_template("index.html", quote=text, author=author)


if __name__ == '__main__':
    app.run()
