from flask import Flask
from flask_moment import Moment
from config import config

moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    moment.init_app(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


