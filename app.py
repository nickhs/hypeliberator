from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from os import getenv


def get_config():
    status = getenv("LIBERATOR_CONFIG", '').lower()

    if 'prod' in status:
        selected_config = "ProductionConfig"

    elif 'dev' in status:
        selected_config = "DevelopmentConfig"

    else:
        # FIXME print warning here
        selected_config = "Config"

    return "settings." + selected_config

app = Flask(__name__)
app.config.from_object(get_config())
config = app.config

db = SQLAlchemy(app)
