from flask import Flask
from projectrad.views import views
from projectrad.db import db

from os.path import join as path_join
from os import makedirs


def create_app(test_config: dict | None = None):
    app = Flask(__name__)
    app.register_blueprint(views)

    if test_config is None:
        app.config.update(
            SQL_ALCHEMY_DATABASE="sqlite:///app.db",
            SESSION_COOKIE_HTTPONLY=True,
            UPLOAD_FOLDER=path_join(app.instance_path, 'uploads')
        )
    else:
        app.config.update(**test_config)

    makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    create_app().run("0.0.0.0", 5000, True)

