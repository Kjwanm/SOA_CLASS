import requests
from flask import Flask, render_template, request, Blueprint

from keys import KAKAO_REST_KEY

KAKAO_BASE_URL="https://dapi.kakao.com"

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
    headers = {"Authorization": "KakaoAK " + KAKAO_REST_KEY}

    res2 = requests.get(
        url=KAKAO_BASE_URL + "/v2/search/image?query=파이썬",
        headers=headers
    )

    if res2.status_code == 200:
        docs = res2.json()
        images = []
        for image in docs['documents']:
            images.append(image['image_url'])

        print(images)

    else:
        print("Error {0}".format(res2.status_code))

    return render_template(
        'images.html', images=images, nav_menu="image"
    )