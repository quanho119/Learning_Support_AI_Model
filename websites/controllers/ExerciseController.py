import os

from flask import Blueprint, render_template, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename

from websites.entities.Excercise import Exercise
from websites.models.ExcerciseModel import exercises
from websites.tools.chatBot.chatbot import ChatBotAi
bp = Blueprint('exercises', __name__, url_prefix='/teachers/exercises')

exerciseAdd = Exercise(max(exercises, key=lambda exercise: exercise.id).id + 1, "", "", "")
@bp.route("/")
def render_list():
    exerciseAdd.set_name("")
    exerciseAdd.set_description("")
    exerciseAdd.set_question("")
    return render_template("teachers/exercises/list.html", exercises=exercises)


@bp.route("/full/<int:id>")
def render_full_exercise(id):
    for exercise in exercises:
        if exercise.id == id:
            return render_template("teachers/exercises/full.html", exercise=exercise)
    return redirect(url_for('exercises.renderList'))


@bp.route('/add', methods=['GET'])
def renderAdd():
    return render_template("teachers/exercises/add.html", exercise=exerciseAdd)


@bp.route("/add", methods=['POST'])
def add():
    id = max(exercises, key=lambda exercise: exercise.id).id + 1
    name = request.form.get('name')
    description = request.form.get('description')
    question = request.form.get('question')
    exercise = Exercise(id, name, description, question)
    exercises.append(exercise)
    return redirect(url_for('exercises.render_list'))


@bp.route('/delete/<int:id>')
def delete(id):
    for exercise in exercises:
        if exercise.id == id:
            exercises.remove(exercise)
            break
    return redirect(url_for('exercises.renderList'))


@bp.route('/edit/<int:id>')
def renderEdit(id):
    for exercise in exercises:
        if exercise.id == id:
            return render_template("teachers/exercises/edit.html", exercise=exercise)


@bp.route('/edit/', methods=['POST'])
def edit():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    question = request.form.get('question')

    for exercise in exercises:
        if exercise.id == int(id):
            exercise.set_name(name)
            exercise.set_description(description)
            exercise.set_question(question)
            break
    return redirect(url_for('exercises.render_list'))

@bp.route('/add/upload/<value>', methods=['GET'])
def renderUploadForAdd(value):
    return render_template("teachers/exercises/addImage.html", value=value)

@bp.route('/add/upload/<value>', methods=['POST'])
def AddUpload(value):
    file = request.files['file']
    upload_path=current_app.config['UPLOAD_FOLDER']
    new_filename = f"upload.png"
    os.makedirs(upload_path, exist_ok=True)
    save_path = os.path.join(upload_path, new_filename)
    file.save(save_path)
    response = Convert()
    match value:
        case "name":
            exerciseAdd.set_name(response)
        case "description":
            exerciseAdd.set_description(response)
        case "question":
            exerciseAdd.set_question(response)
    return redirect(url_for('exercises.renderAdd'))

def Convert(self=None):
    response = ChatBotAi.convert_image_to_text(self)
    return response

@bp.route('/edit/<int:id>/upload/<value>', methods=['GET'])
def renderUploadForEdit(id,value):
    return render_template("teachers/exercises/editImage.html", value=value, id=id)

@bp.route('/edit/<int:id>/upload/<value>', methods=['POST'])
def EditUpload(id,value):

    file = request.files['file']
    upload_path=current_app.config['UPLOAD_FOLDER']
    new_filename = f"upload.png"
    os.makedirs(upload_path, exist_ok=True)
    save_path = os.path.join(upload_path, new_filename)
    file.save(save_path)
    response = Convert()
    for exercise in exercises:
        if exercise.id == id:
            match value:
                case "name":
                    exercise.set_name(response)
                case "description":
                    exercise.set_description(response)
                case "question":
                    exercise.set_question(response)
    return redirect(url_for('exercises.renderEdit', id=id))