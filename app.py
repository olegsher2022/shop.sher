from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/soul_ceramics')
def soul_ceramics():
    return render_template('soul_ceramics.html')
