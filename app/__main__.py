from flask import Flask
from flask_script import Manager


def register_blueprints(app):
    from .api.hello import hello_handler

    app.register_blueprint(hello_handler, url_prefix="")


def create_base_app():
    app = Flask("app")
    register_blueprints(app)
    return app


def run_cli():
    app = create_base_app()

    cli = Manager(app)
    cli.run()
