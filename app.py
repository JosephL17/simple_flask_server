from flask import Flask, jsonify
from students_data import students

#initializes a variable to create a Flask instance and we pass it the name of the current module or __name__
app = Flask(__name__)

# Use the decorator to define a route
@app.route("/")
def get_students():
    return jsonify(students)

# Use the decorator to define a route /old_students/
@app.route("/old_students/")
def get_old_students():
    students_over_20 = [student for student in students if student['age'] > 20]
    return jsonify(students_over_20)

# Use the decorator to define a route /young_students/
@app.route("/young_students/")
def get_young_students():
    students_under_20 = [student for student in students if student['age'] < 20]
    return jsonify(students_under_20)

# Use the decorator to define a route /advanced_students/
@app.route("/advance_students/")
def get_advanced_students():
    students_advanced = [student for student in students if student['grade'] == 'A']
    return jsonify(students_advanced)

# Use the decorator to define a route /student_names/
@app.route("/student_names/")
def get_names():
    student_names = []
    for student in students:
        student_names.append({'first_name': student['first_name'], 'last_name': student['last_name']})
    return jsonify(student_names)

# Use the decorator to define a route /students_age/
@app.route("/students_age")
def get_age():
    student_ages = []
    for student in students:
        student_ages.append({'first_name': student['first_name'], 'last_name': student['last_name'], 'age': student['age']})
    return jsonify(student_ages)





# This start the Flask app with app.run(debug=True). the server defaults to http://localhost:5000/
app.run(debug=True)

