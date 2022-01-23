import os
from flask import Flask, request
from flask_restx import abort
from funtions import get_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

#TODO: make schema & validation

@app.route("/perform_query")
def perform_query():
    try:
        query = request.args["query"]
        file_name = request.args["file_name"]
        file_ = os.path.join(DATA_DIR, file_name)
        if not file_:
            raise FileExistsError

        with open(file_, "r") as file:
            data = file.readlines()
        result = get_query(data, query)
        return app.response_class(result, content_type="text/plain")
    except (KeyError, IndexError, IsADirectoryError, FileExistsError):
        abort(400), 'error'


if __name__ == "__main__":
    app.run(port=5007)
