from flask import make_response, request
from flask_restful import Resource

from db import session
from models import UserModel
from schemas import UserSchema


class userResource(Resource):
    ### get user , method : get###
    def get(self):
        filters = {}
        if 'phone' in request.args:
            filters['phone'] = request.args.get('phone')
        if 'username' in request.args:
            filters['username'] = request.args.get('username')
        if 'email' in request.args:
            filters['email'] = request.args.get('email')
        print(filters)
        user_modal = UserModel()
        users = user_modal.get_all(filters)
        user_jsons = user_modal.jsonif(users, UserSchema, many=True)
        return make_response({"users": user_jsons}, 200)

    def post(self):
        ### create user , method : post ###
        user = request.get_json()
        user_data = UserModel(user)

        session.add(user_data)
        session.commit()

        user_schema = UserSchema()
        user_json = user_schema.dump(user_data)
        return make_response(user_json, 201)

    def put(self):
        ### update user , method : put ###=
        user = request.get_json()
        user.update({"id": 1})
        return make_response({"id": 1, "name": "Hoeur Lihour"}, 200)

    def patch(self):
        ### update user , method : patch ###
        user = request.get_json()
        return make_response(user, 201)

    def delete(self):
        ### delete user , method : delete ###
        return make_response("user delete successfully", 204)
