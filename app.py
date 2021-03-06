import os
from flask import Flask, request, Response
from werkzeug.exceptions import BadRequest

from funtions import get_query
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


class Validator(Schema):
    query = fields.Str(request=True)
    file_name = fields.Str(request=True)


@app.route("/perform_query")
def perform_query() -> Response:
    try:
        data = Validator().load(request.args)
        file_ = os.path.join(DATA_DIR, data['file_name'])
        if not file_:
            raise FileExistsError

        with open(file_, "r") as file:
            file_read = file.readlines()

        result = get_query(file_read, data['query'])
        return app.response_class(result, content_type="text/plain")

    except (KeyError, IndexError, IsADirectoryError, FileExistsError, ValidationError, NotImplementedError):
        raise BadRequest(description='error')


if __name__ == "__main__":
    app.run(port=5000)
