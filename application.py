from flask import Flask, render_template, request
import logging
import os

from database import base
from database.base import User
from news import news_blueprint
from rest_server.resource import TemperatureResource, TemperatureCreationResource, TemperatureByLocationResource
from rest_server.resource_check import resource_blueprint
from flask_restful import Api

from flask_login import current_user, LoginManager

from keys import KAKAO_REST_KEY

application = Flask(__name__)
application.register_blueprint(news_blueprint, url_prefix='/news')
application.register_blueprint(resource_blueprint, url_prefix='/resource')

api = Api(application)
api.add_resource(TemperatureResource, "/resource/<sensor_id>")
api.add_resource(TemperatureCreationResource, "/resource_creation")
api.add_resource(TemperatureByLocationResource, "/resource_location/<location>")


application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(application)

logging.basicConfig(filename='test.log', level=logging.DEBUG)

@login_manager.user_loader
def load_user(user_id):
    q = base.db_session.query(User).filter(User.id == user_id)
    user = q.first()

    if user is not None:
        user._authenticated = True
    return user


@application.route('/')
def hello_html():
    value = 50
    value_list = ['파이썬', '자바', '스위프트']

    return render_template(
        'index.html',
        name="jwkim",
        value_list=value_list,
        value=value,
        current_user=current_user
    )


if __name__ == "__main__":
    logging.info("Flask Web Server Started!!!")

    application.debug = True
    application.config['DEBUG'] = True

    application.run(host="localhost", port="8777")