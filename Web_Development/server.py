from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.getcwd(), static_folder='assets')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'Blog blah blah'