import pprint
import requests
import sqlite3

from keys import KEY

BASE_URL="https://openapi.gg.go.kr/Tbinstutm"
BASE_URL_2="https://openapi.gg.go.kr/GgSchoolM"

insertion_data = """
    INSERT INTO EDUCATION VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

if __name__ == "__main__":

    res3 = requests.get(
        url=BASE_URL + "?Key=" + KEY + "&Type=json&pIndex=1&pSize=500&SIGUN_NM=오산시"
    )
    if res3.status_code == 200:
        docs = res3.json()
        for item in docs['Tbinstutm'][1]['row']:
            pprint.pprint(item)
            sigun = item['SIGUN_NM']
            emd = item['EMD_NM']
            types = item['CRSE_CLASS_NM']
            named = item['FACLT_NM']
            daepyo = item['REPRSNTV_NM']
            telno = item['TELNO']
            address = item['REFINE_ROADNM_ADDR']
            lat = item['REFINE_WGS84_LAT']
            loat = item['REFINE_WGS84_LOGT']
            conn = sqlite3.connect('soa2.db')
            cur = conn.cursor()
            cur.execute(
                insertion_data,
                (sigun, emd, types, named, daepyo, telno, address, lat, loat)
            )
            conn.commit()
            conn.close()

        else:
            print("Error {0}".format(res3.status_code))

    res4 = requests.get(
        url=BASE_URL_2 + "?Key=" + KEY + "&Type=json&pIndex=1&pSize=500&SIGUN_NM=오산시"
    )
    if res4.status_code == 200:
        docs = res4.json()
        for item in docs['GgSchoolM'][1]['row']:
            pprint.pprint(item)
            sigun = item['SIGUN_NM']
            emd = item['SIGUN_CD']
            types = item['SCHOOL_DIV_NM']
            named = item['FACLT_NM']
            daepyo = item['PLVTINST_DIV_NM']
            telno = item['TELNO']
            address = item['REFINE_ROADNM_ADDR']
            lat = item['REFINE_WGS84_LAT']
            loat = item['REFINE_WGS84_LOGT']
            conn = sqlite3.connect('soa2.db')
            cur = conn.cursor()
            cur.execute(
                insertion_data,
                (sigun, emd, types, named, daepyo, telno, address, lat, loat)
            )
            conn.commit()
            conn.close()

        else:
            print("Error {0}".format(res4.status_code))