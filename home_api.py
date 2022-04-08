"""
Created on Fri Dec  3 09:03:58 2021

@author: p_teg
"""

# Get libraries
from flask import Flask
from flask_restful import Resource, Api, reqparse

# Initialise API
app = Flask(__name__)
api = Api(app)
STUDENTS = {}

# Mock data
STUDENTS = {
    '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
    '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
    '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
    '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
}

# Parser
parser = reqparse.RequestParser()

# Endpoint
class StudentsList(Resource):
  
    # Methods
    def get(self):
        return STUDENTS
    
    def post(self):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("spec")
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"],
            }
        return STUDENTS[student_id], 201

# Path to endpoint      
api.add_resource(StudentsList, '/students/')

# Run local server
if __name__ == "__main__":
    app.run()