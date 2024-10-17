from flask import Blueprint, render_template, redirect, url_for, request
from websites.models.TeachersModel import students
from websites.entities.Student import Student

bp = Blueprint('teachers', __name__, url_prefix='/teachers/')


@bp.route('/')
def renderList():
    return render_template("teachers/list.html", students=students)


@bp.route('/add', methods=['GET'])
def renderAdd():
    return render_template("teachers/add.html")


@bp.route('/add', methods=['POST'])
def add():
    id = max(students, key=lambda student: student.id).id + 1
    name = request.form.get('name')
    student = Student(id, name)
    students.append(student)
    return redirect(url_for('teachers.renderList'))


@bp.route('/delete/<int:id>')
def delete(id):
    for student in students:
        if student.id == id:
            students.remove(student)
            break
    return redirect(url_for('teachers.renderList'))


@bp.route('/edit/<int:id>')
def renderEdit(id):
    for student in students:
        if student.id == id:
            return render_template("teachers/edit.html", student=student)


@bp.route('/edit/', methods=['POST'])
def edit():
    id = request.form.get('id')
    name = request.form.get('name')
    for student in students:
        if student.id == int(id):
            student.set_name(name)
            break
    return redirect(url_for('teachers.renderList'))

