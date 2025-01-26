from flask import make_response, request
from flask_restful import Resource

from db import session
from models import UserModel
from schemas import UserSchema

class userResource(Resource):
    ### get user , method : get###
    def get(self):
        users = session.query(UserModel).all()
        
        user_schema = UserSchema()
        user_json = user_schema.dump(users, many=True)
        return make_response({
            "users": user_json
            }, 200)
        
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
        user.update({
            "id" : 1
        })
        return make_response({
                "id" : 1,
                "name" : "Hoeur Lihour"
            }, 200)
            
    def patch(self):
        ### update user , method : patch ###
        user = request.get_json()
        return make_response(user, 201)
    
    def delete(self):
        ### delete user , method : delete ###
        return make_response("user delete successfully", 204)