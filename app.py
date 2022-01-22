import os

from flask import Flask, request
from flask_restx import abort
from funtions import get_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    try:
        query = request.args["query"]
        file_name = request.args["file_name"]
    except (KeyError, IndexError):
        abort(400), 'error'

    file_ = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_):
        abort(400), 'error'
    try:
        with open(file_, "r") as file:
            result = get_query(file, query)
    except IsADirectoryError:
        abort(400), 'error'

    return app.response_class(result, content_type="text/plain")


if __name__ == "__main__":
    app.run(port=5007)
