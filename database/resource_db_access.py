#-*- coding:cp949 -*-

import sqlite3
import math

insertion_resource = """
    INSERT INTO EDUCATION VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

selection_resource_by_location = """
    SELECT * FROM EDUCATION WHERE sigun=?
"""

selection_resource_by_emd = """
    SELECT * FROM EDUCATION WHERE emd LIKE ?
"""

selection_resource_by_name = """
    SELECT * FROM EDUCATION WHERE named LIKE ?
"""

selection_resource_by_distance = """
    SELECT * FROM EDUCATION WHERE (lat BETWEEN ? AND ?) AND (loat BETWEEN ? AND ?) 
"""

update_resource_by_name = """
    UPDATE EDUCATION SET sigun=?, emd=?, types=?, daepyo=?, telno=?, address=?, lat=?, loat=? WHERE named=?
"""

delete_resource_by_name = """
    DELETE FROM EDUCATION WHERE named = ?
"""



class EducationResourceDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('database/soa2.db')

    def crate(self, sigun, emd, types, named, daepyo, telno, address, lat, loat):
        cur = self.conn.cursor()
        cur.execute(
            insertion_resource,
            (sigun, emd, types, named, daepyo, telno, address, lat, loat)
        )
        self.conn.commit()

    def update(self, sigun, emd, types, daepyo, telno, address, lat, loat):
        cur = self.conn.cursor()
        cur.execute(
            update_resource_by_name,
            (sigun, emd, types, daepyo, telno, address, lat, loat)
        )
        self.conn.commit()

    def delete(self, named):
        cur = self.conn.cursor()
        cur.execute(
            delete_resource_by_name, (named,)
        )
        self.conn.commit()

    def readByLocation(self, sigun):
        cur = self.conn.cursor()
        cur.execute(
            selection_resource_by_location, (sigun,)
        )
        row = cur.fetchall()
        if row:
            education = []
            for now in row:
                tsigun = now[1]
                temd = now[2]
                ttypes = now[3]
                tnamed = now[4]
                tdaepyo = now[5]
                ttelno = now[6]
                taddress = now[7]
                tlat = now[8]
                tloat = now[9]
                education.append({
                    "sigun": tsigun,
                    "emd": temd,
                    "types": ttypes,
                    "named": tnamed,
                    "daepyo": tdaepyo,
                    "telno": ttelno,
                    "address": taddress,
                    "lat": tlat,
                    "loat": tloat
                })
        else:
            education = None
        self.conn.commit()
        return education

    def readByEMD(self, emd):
        cur = self.conn.cursor()
        cur.execute(
            selection_resource_by_emd, (emd,)
        )
        row = cur.fetchall()
        if row:
            education = []
            for now in row:
                tsigun = now[1]
                temd = now[2]
                ttypes = now[3]
                tnamed = now[4]
                tdaepyo = now[5]
                ttelno = now[6]
                taddress = now[7]
                tlat = now[8]
                tloat = now[9]
                education.append({
                    "sigun": tsigun,
                    "emd": temd,
                    "types": ttypes,
                    "named": tnamed,
                    "daepyo": tdaepyo,
                    "telno": ttelno,
                    "address": taddress,
                    "lat": tlat,
                    "loat": tloat
                })
        else:
            education = None

        self.conn.commit()
        return education

    def readByNamed(self, named):
        cur = self.conn.cursor()
        cur.execute(
            selection_resource_by_name, (named,)
        )
        row = cur.fetchone()
        if row:
            print(row)
            education = []
            tsigun = row[1]
            temd = row[2]
            ttypes = row[3]
            tnamed = row[4]
            tdaepyo = row[5]
            ttelno = row[6]
            taddress = row[7]
            tlat = row[8]
            tloat = row[9]
            education.append({
                "sigun": tsigun,
                "emd": temd,
                "types": ttypes,
                "named": tnamed,
                "daepyo": tdaepyo,
                "telno": ttelno,
                "address": taddress,
                "lat": tlat,
                "loat": tloat
            })
        else:
            education = None
        self.conn.commit()
        return education

    def readByDistance(self, named):
        cur = self.conn.cursor()
        cur.execute(
            selection_resource_by_name, (named,)
        )
        row = cur.fetchone()
        if row:
            education = []
            tlat = row[8]
            tloat = row[9]
            ptloat = float(tloat) + 5 * (0.007 * math.cos(0))
            ptlat = float(tlat) + 5 * (0.007 * math.sin(90))
            minlat = str(float(tlat) - (ptlat - float(tlat)))
            maxlat = str(ptlat)
            minloat = str(float(tloat) - (ptloat - float(tloat)))
            maxloat = str(ptloat)
            print(tloat)
            print(minloat)
            print(maxloat)
            print(tlat)
            print(minlat)
            print(maxlat)
            cur.execute(
                selection_resource_by_distance, (minlat, maxlat, minloat, maxloat)
            )
            result = cur.fetchall()
            if result:
                for now in result:
                    tsigun = now[1]
                    temd = now[2]
                    ttypes = now[3]
                    tnamed = now[4]
                    tdaepyo = now[5]
                    ttelno = now[6]
                    taddress = now[7]
                    tlat = now[8]
                    tloat = now[9]
                    education.append({
                        "sigun": tsigun,
                        "emd": temd,
                        "types": ttypes,
                        "named": tnamed,
                        "daepyo": tdaepyo,
                        "telno": ttelno,
                        "address": taddress,
                        "lat": tlat,
                        "loat": tloat
                })
            else :
                education = None
        else:
            education = None
        self.conn.commit()
        return education