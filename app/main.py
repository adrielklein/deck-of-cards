from flask import Flask

from app.routes import AcknowledgeRoute, AddCardRoute, DrawCardRoute, ShuffleRoute, ResetRoute, CardsLeftRoute


def _set_up_routes(routes, app):
    for route in routes:
        app.add_url_rule(route.path, route.endpoint, route.handle, methods=[route.method])


def create_app(deck):
    app = Flask(__name__)
    routes = [AcknowledgeRoute(),
              AddCardRoute(deck),
              DrawCardRoute(deck),
              ShuffleRoute(deck),
              ResetRoute(deck),
              CardsLeftRoute(deck)]
    _set_up_routes(routes, app)

    return app
