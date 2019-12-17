#-*- coding:cp949 -*-
import json

from flask import make_response, render_template, jsonify, Response
from flask.json import dumps
from flask_restful import Resource, abort, reqparse

from database.resource_db_access import EducationResourceDatabase


class EducationResource(Resource):
    def __init__(self):
        self.education_resource_db = EducationResourceDatabase()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('sigun')
        self.parser.add_argument('emd')
        self.parser.add_argument('types')
        self.parser.add_argument('named')
        self.parser.add_argument('daepyo')
        self.parser.add_argument('telno')
        self.parser.add_argument('address')
        self.parser.add_argument('lat')
        self.parser.add_argument('loat')

    def get(self, named):
        education = self.education_resource_db.readByNamed(named=named)
        print(education)
        if education is None:
            return Response("이름 : {0} 가 존재하지 않습니다.".format(named), status=404, mimetype='application/json; charset=utf-8')
        else:
            return Response(dumps(education, ensure_ascii=False), content_type='application/json; charset=utf-8')

    def put(self, named):
        args = self.parser.parse_args()
        education = self.education_resource_db.readByNamed(named=named)
        if education is None:
            return Response("이름 : {0} 가 존재하지 않습니다.".format(named), status=404, mimetype='application/json; charset=utf-8')
        else:
            self.education_resource_db.update(
                sigun=args['sigun'],
                emd=args['emd'],
                types=args['types'],
                daepyo=args['daepyo'],
                telno=args['telno'],
                address=args['address'],
                lat=args['lat'],
                loat=args['loat']
            )
            return Response("이름 : {0},".format(named), status=200, mimetype='application/json; charset=utf-8')

    def delete(self, named):
        education = self.education_resource_db.readByNamed(named=named)
        if education is None:
            return Response("이름 : {0},".format(named), status=204, mimetype='application/json; charset=utf-8')
        else:
            self.education_resource_db.delete(named=named)
            return Response("이름 : {0},".format(named), status=204, mimetype='application/json; charset=utf-8')


class EducationCreationResource(Resource):
    def __init__(self):
        self.education_resource_db = EducationResourceDatabase()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('sigun')
        self.parser.add_argument('emd')
        self.parser.add_argument('types')
        self.parser.add_argument('named')
        self.parser.add_argument('daepyo')
        self.parser.add_argument('telno')
        self.parser.add_argument('address')
        self.parser.add_argument('lat')
        self.parser.add_argument('loat')

    def post(self):
        args = self.parser.parse_args()
        named = args['named']
        education = self.education_resource_db.readByNamed(named=named)
        if education is not None:
            return Response("이름 : {0}가 이미 존재합니다!!,".format(named), status=409, mimetype='application/json; charset=utf-8')
        else:
            self.education_resource_db.crate(
                sigun=args['sigun'],
                emd=args['emd'],
                types=args['types'],
                named=named,
                daepyo=args['daepyo'],
                telno=args['telno'],
                address=args['address'],
                lat=args['lat'],
                loat=args['loat']
            )
            return Response("이름 : {0},".format(named), status=201, mimetype='application/json; charset=utf-8')


class EducationByLocationResource(Resource):
    def __init__(self):
        self.education_resource_db = EducationResourceDatabase()

    def get(self, sigun):
        education = self.education_resource_db.readByLocation(sigun=sigun)
        if education is None:
            # abort(404, message="sigun {0} doesn't exist".format(sigun))
            return Response("시군정보 : {0} 가 존재하지 않습니다.".format(sigun), status=404, mimetype='application/json; charset=utf-8')
        else:
            return Response(dumps(education, ensure_ascii=False), content_type='application/json; charset=utf-8')


class EducationByEMDResource(Resource):
    def __init__(self):
        self.education_resource_db = EducationResourceDatabase()

    def get(self, emd):
        education = self.education_resource_db.readByEMD(emd=emd)
        if education is None:
            return Response("읍면동 : {0} 가 존재하지 않습니다.".format(emd), status=404, mimetype='application/json; charset=utf-8')
        else:
            return Response(dumps(education, ensure_ascii=False), content_type='application/json; charset=utf-8')

class EducationByDistance(Resource):
    def __init__(self):
        self.education_resource_db = EducationResourceDatabase()

    def get(self, named):
        education = self.education_resource_db.readByDistance(named=named)
        if education is None:
            return Response("해당하는 학원 : {0} 가 존재하지 않습니다.".format(named), status=404, mimetype='application/json; charset=utf-8')
        else:
            return Response(dumps(education, ensure_ascii=False), content_type='application/json; charset=utf-8')