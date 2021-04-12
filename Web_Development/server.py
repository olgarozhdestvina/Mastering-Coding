from flask import Flask, render_template
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError
import os

app = Flask(__name__, template_folder=os.getcwd(), static_folder='assets')

@app.route('/')
def index():
    return render_template('index.html')

# Error handlers.
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'Bad request!', 400


@app.errorhandler(NotFound)
def handle_bad_request1(e):
    return 'Page is not found!', 404


@app.errorhandler(MethodNotAllowed)
def handle_bad_request2(e):
    return 'Method is not allowed!', 405


@app.errorhandler(InternalServerError)
def handle_bad_request3(e):
    return 'Internal server error!', 500

if __name__ == '__main__':
    app.run(debug=True)