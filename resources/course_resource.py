from flask import make_response, request
from flask_restful import Resource

class courseResource(Resource):
    ### get course , method : get###
    def get(self, id=None):
        return make_response({
            "user" : {
                "title" : "Flask Course"
            }
        }, 200)
        
    def post(self):
        ### create course , method : post ###
        print(request)
        course = request.get_json()
        return make_response(course, 201)
    
    def put(self):
        ### update course , method : put ###=
        course = request.get_json()
        course.update({
            "id" : 1
        })
        return make_response(course, 200)
            
    def patch(self):
        ### update course , method : patch ###
        course = request.get_json()
        return make_response(course, 201)
    
    def delete(self):
        ### delete course , method : delete ###
        return make_response("course delete successfully", 204)