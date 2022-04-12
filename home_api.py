"""
Created on Fri Dec  3 09:03:58 2021

@author: p_teg
"""

# Get libraries
from flask import Flask, request
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

# Parser for json requests
parser = reqparse.RequestParser()

class StudentsList(Resource):
  
    # Return student list
    def get(self):
        return STUDENTS
    
    # New student
    def post(self):
        # Read name from query
        print(request.args.get('name'))
        
        parser.add_argument('name')
        parser.add_argument('age')
        parser.add_argument('spec')
        args = parser.parse_args()
        print('test')
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

class Student(Resource):

    # Return student
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]

    # Update student
    def put(self, student_id):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("spec")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["name"] = args["name"] if args["name"] is not None else student["name"]
            student["age"] = args["age"] if args["age"] is not None else student["age"]
            student["spec"] = args["spec"] if args["spec"] is not None else student["spec"]
        return student, 200

    # Delete student
    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
        return '', 204

api.add_resource(Student, '/students/<student_id>')

# Run local server
if __name__ == "__main__":
    app.run(debug=True)