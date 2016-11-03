from flask import Flask

from routes import AcknowledgeRoute


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle)


def create_app():
    app = Flask(__name__)
    routes = [AcknowledgeRoute()]
    _set_up_routes(routes, app)

    return app