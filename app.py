from flask import Flask, render_template, request
from spellcheck import correct_sentence_trigram

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    original = ""
    corrected = ""
    if request.method == 'POST':
        original = request.form['text']
        corrected = correct_sentence_trigram(original)
    return render_template('index.html', original=original, corrected=corrected)

if __name__ == '__main__':
    app.run(debug=True)
