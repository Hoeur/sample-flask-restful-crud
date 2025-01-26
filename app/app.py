from flask import Flask, Blueprint
from routes import *
app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Hello World!"    

print(globals().values())

[app.register_blueprint(route) for route in globals().values() if isinstance(route, Blueprint)]
# app.register_blueprint(user_route)
# app.register_blueprint(course_route)