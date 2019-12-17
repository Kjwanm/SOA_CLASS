#-*- coding:utf-8 -*-
from flask import Flask, render_template
import logging


from news import news_blueprint
from rest_server.resource import EducationResource, EducationCreationResource, EducationByLocationResource, EducationByEMDResource, EducationByDistance
from rest_server.resource_check import resource_blueprint
from flask_restful import Api


application = Flask(__name__)
application.register_blueprint(news_blueprint, url_prefix='/news')
application.register_blueprint(resource_blueprint, url_prefix='/resource')

api = Api(application)
api.add_resource(EducationResource, "/resource/<named>")
api.add_resource(EducationCreationResource, "/resource_creation")
api.add_resource(EducationByLocationResource, "/resource_location/<sigun>")
api.add_resource(EducationByEMDResource, "/resource_emd/<emd>")
api.add_resource(EducationByDistance, "/resource_distance/<named>")

logging.basicConfig(filename='test.log', level=logging.DEBUG)



@application.route('/')
def hello_html():

    return render_template(
        'index.html',
    )


if __name__ == "__main__":
    logging.info("Flask Web Server Started!!!")

    application.debug = True
    application.config['DEBUG'] = True

    application.run(host="localhost", port="8777")