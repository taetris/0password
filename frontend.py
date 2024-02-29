from flask import Flask, render_template, request
from src.pwgenerate import generate_password
from src.main import push, pull
from src.clipboard import copy_to_clipboard
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    password = push()

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
