from flask import Flask, render_template, request
from AIanalasys import classify_threat  # Assuming classify_threat is in model.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    message = request.form['message']
    result = classify_threat(message)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)