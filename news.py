import requests
from flask import Flask, render_template, request, Blueprint

news_blueprint = Blueprint('news', __name__)


@news_blueprint.route('/main')
def news_main():
    return 'welcome news {0}'.format("yhhan")


@news_blueprint.route('/sports')
def news_sports():
    return 'welcome sports news {0}'.format("yhhan")


@news_blueprint.route('/science')
def news_science():
    return 'welcome science news {0}'.format("yhhan")

@news_blueprint.route('/images')
def images():
    return render_template('images.html')

@news_blueprint.route('/rest')
def rests():
    return render_template('rest.html')

@news_blueprint.route('/example')
def examples():
    res = requests.get(
        url="http://localhost:8777/resource_distance/" +  request.args.get("named")
    )
    value = None
    if res.status_code == 200:
        value = res.json()
    else:
        print("Error {0}".format(res.status_code))

    return render_template(
        'example.html', value=value
    )

@news_blueprint.route('/location')
def locations():
    res = requests.get(
        url="http://localhost:8777/resource_location/" +  request.args.get("sigun")
    )
    value = None
    if res.status_code == 200:
        value = res.json()
    else:
        print("Error {0}".format(res.status_code))

    return render_template(
        'example.html', value=value
    )

@news_blueprint.route('/emd')
def emd():
    res = requests.get(
        url="http://localhost:8777/resource_emd/" +  request.args.get("emd")
    )
    value = None
    if res.status_code == 200:
        value = res.json()
    else:
        print("Error {0}".format(res.status_code))

    return render_template(
        'example.html', value=value
    )

@news_blueprint.route('/name')
def name():
    res = requests.get(
        url="http://localhost:8777/resource/" +  request.args.get("named")
    )
    value = None
    if res.status_code == 200:
        value = res.json()
    else:
        print("Error {0}".format(res.status_code))

    return render_template(
        'example.html', value=value
    )