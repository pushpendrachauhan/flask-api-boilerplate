# app/__init__.py

from flask import Flask

# local import
from instance.config import app_config
import config

from controllers import user_controller,campaign_controller
from models import database
# initialize sql-alchemy
#db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    if config_name:
    	app.config.from_object(app_config[config_name])
    else:
    	app.config.from_object('config')

    app.register_blueprint(user_controller.bp)
    app.register_blueprint(campaign_controller.bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        print "context called"
        database.db_session.remove()

    return app