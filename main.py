from flask import Flask

from routes import AcknowledgeRoute, AddCardRoute, GetCardRoute


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle, methods=[route.method])


def create_app(deck):
    app = Flask(__name__)
    routes = [AcknowledgeRoute(), AddCardRoute(deck), GetCardRoute(deck)]
    _set_up_routes(routes, app)

    return app
