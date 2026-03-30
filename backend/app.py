from flask import Flask, request, jsonify
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'GET':
        students = Student.query.all()
        return jsonify([{'id': s.id, 'name': s.name, 'grade': s.grade} for s in students])
    elif request.method == 'POST':
        data = request.get_json()
        new_student = Student(name=data['name'], grade=data['grade'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student added'}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
