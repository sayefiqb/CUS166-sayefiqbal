from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String(10), nullable=False, default='CUS1166')
    course_title = db.Column(db.String(30), nullable=False, default='Software Engineering')
    registered_students = db.relationship('RegisteredStudent', backref='students', lazy=True)

class RegisteredStudent(db.Model):
    __tablename__ = 'registered_student'
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(20), nullable=False)
    student_grade = db.Column(db.Integer, nullable=False)
    student_course = db.Column(db.Integer, db.ForeignKey(Course.course_id), nullable=False)
