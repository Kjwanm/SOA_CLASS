#-*- coding:utf-8 -*-
import sqlite3
from flask import Blueprint, render_template


resource_blueprint = Blueprint('resource', __name__)

select_sample_data = """
    SELECT * FROM EDUCATION;
"""


@resource_blueprint.route("/resource_check")
def resource_check():
    conn = sqlite3.connect('database/soa2.db')
    cur = conn.cursor()
    cur.execute(select_sample_data)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return render_template("resource_check.html", resources=rows)