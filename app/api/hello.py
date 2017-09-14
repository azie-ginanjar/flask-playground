from flask import Blueprint

hello_handler = Blueprint("hello_handler", __name__)


@hello_handler.route("/", methods=["GET"])
def index():
    return "Hello World"
