from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

#connecting data to database
client=MongoClient('mongodb://localhost:27017')
db=client['RAM']
collection=db['registration']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/count_lines', methods=['POST'])
def count_lines():
    text = request.form['text']
    lines = len(text.split('\n'))
    return render_template('count.html', lines=lines)
""""@app.route('/count_words', methods=['POST'])
def count_words():
    text=request.form['word']
    words=len(words.split())
    return render_template('count.html',words=words)"""""

if __name__ == '__main__':
    app.run(debug=True)
