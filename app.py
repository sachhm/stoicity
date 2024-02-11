"""
app.py

main web app
"""

from flask import Flask
from flask import render_template, url_for

import quote_reader

app = Flask(__name__)


@app.route('/')
def home():
    quote = quote_reader.get_random_quote()
    text=quote['text']
    author=quote['author']
    return render_template("index.html", quote=text, author=author)


if __name__ == '__main__':
    app.run()
