import sys

from flask import Flask, render_template, url_for
from flask_frozen import Freezer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/faq/')
# @app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/install/')
# @app.route('/install.html')
def install():
    return render_template('install.html')

if __name__ == '__main__':
    app.run(port=1122, debug=True)
