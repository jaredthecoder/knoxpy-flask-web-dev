# -*- coding: utf-8 -*-


"""The app module, containing the app factory function."""


import os

from flask import Flask, render_template

from redzone import public, user
from redzone.assets import assets
from redzone.extensions import bcrypt, cache, db
from redzone.extensions import debug_toolbar, login_manager, migrate
from redzone.settings import ProdConfig


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """

    app = Flask(__name__)
    config_object = os.environ["REDZONE_SETTINGS"] or config_object
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""

    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from redzone.user.models import Anonymous
    login_manager.anonymous_user = Anonymous

    debug_toolbar.init_app(app)
    migrate.init_app(app, db)

    return None


def register_blueprints(app):
    """Register Flask blueprints."""

    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)

    return None


def register_error_handlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""

        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)

    return None
