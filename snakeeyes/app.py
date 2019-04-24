from flask import Flask
from celery import Celery

from snakeeyes.blueprints.page import page
from snakeeyes.blueprints.contact import contact
from snakeeyes.blueprints.ml import ml
from snakeeyes.blueprints.tc import tc
from snakeeyes.blueprints.survey import survey
from snakeeyes.extensions import debug_toolbar, mail, csrf

from flask_sqlalchemy import SQLAlchemy

CELERY_TASK_LIST = [
    'snakeeyes.blueprints.contact.tasks',
]


def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    #The code below disables the redirect page.
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    if settings_override:
        app.config.update(settings_override)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vinyllib.db'
    app.secret_key = "flask rocks!"

    db = SQLAlchemy(app)


    # registration starts here

    app.register_blueprint(page)
    app.register_blueprint(contact)
    app.register_blueprint(ml)
    app.register_blueprint(tc)
    app.register_blueprint(survey)
    extensions(app)

    @app.after_request
    def add_header(response):
        # response.cache_control.no_store = True
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)

    return None


