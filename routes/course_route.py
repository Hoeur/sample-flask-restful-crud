from flask import Blueprint
from flask_restful import Api

from resources import courseResource

course_route = Blueprint("course_route", __name__)

api = Api(course_route)

api.add_resource(courseResource, "/course","/course/<int:id>")