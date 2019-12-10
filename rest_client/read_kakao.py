import pprint
import requests
from keys import KAKAO_REST_KEY
from keys import KAKAO_REST_KEY_1

KAKAO_BASE_URL="https://dapi.kakao.com"
BASE_URL="https://openapi.gg.go.kr/Tbinstutm"

if __name__ == "__main__":

    headers = {"Authorization" : "KakaoAK " + KAKAO_REST_KEY}

    res = requests.get(
        url=KAKAO_BASE_URL+"/v3/search/book?target=title&query=미움받을 용기",
        headers=headers
    )

    if res.status_code == 200:
        books = res.json()
        # pprint.pprint(books['documents'])
        for book in books['documents']:
            print("{0:50s} - {1:20s}".format(book['title'], str(book['authors'])))
        # for book in books['documents']:
        #     print(book['title'])
    else:
        print("Error {0}".format(res.status_code))

    res2 = requests.get(
        url=KAKAO_BASE_URL + "/v2/search/image?query=설현",
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

    res3 = requests.get(
        url=BASE_URL + "?Key=" + KAKAO_REST_KEY_1 + "&Type=json&pIndex=1&pSize=5&SIGUN_NM=수원시"
    )

    if res3.status_code == 200:
        docs = res3.json()
        print(docs)
    else:
        print("Error {0}".format(res3.status_code))