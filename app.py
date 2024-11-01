from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample in-memory database
students = {}

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200

# Get student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = students.get(id)
    if not student:
        abort(404, description="Student not found")
    return jsonify(student), 200

# Create new student
@app.route('/students', methods=['POST'])
def add_student():
    if not request.json or 'id' not in request.json:
        abort(400, description="Invalid input")
    student = {
        'id': request.json['id'],
        'name': request.json.get('name', ""),
        'grade': request.json.get('grade', ""),
        'email': request.json.get('email', "")
    }
    students[student['id']] = student
    return jsonify(student), 201

# Update student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = students.get(id)
    if not student:
        abort(404, description="Student not found")
    data = request.json
    student.update({
        'name': data.get('name', student['name']),
        'grade': data.get('grade', student['grade']),
        'email': data.get('email', student['email'])
    })
    students[id] = student
    return jsonify(student), 200

# Delete student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id not in students:
        abort(404, description="Student not found")
    del students[id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
