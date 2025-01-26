from flask import make_response, request
from flask_restful import Resource

class userResource(Resource):
    ### get user , method : get###
    def get(self):
        return make_response({
            "user" : {
                "name" : "Hoeur Lihour"
            }
        }, 200)
        
    def post(self):
        ### create user , method : post ###
        print(request)
        user = request.get_json()
        return make_response(user, 201)
    
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