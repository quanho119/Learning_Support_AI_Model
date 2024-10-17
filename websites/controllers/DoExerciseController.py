from flask import Blueprint, render_template, redirect, url_for

from websites.models.ExcerciseModel import exercises
from websites.tools.chatBot.chatbot import ChatBotAi

bp = Blueprint('Do_exercise', __name__, url_prefix='/students/exercises')


@bp.route("/")
def render_list():
    return render_template("students/exercises/list.html", exercises=exercises)


@bp.route("/full/<int:id>")
def render_full_exercise(id):
    for exercise in exercises:
        if exercise.id == id:
            return render_template("students/exercises/full.html", exercise=exercise, response=None)
    return redirect(url_for('Do_exercise.renderList'))


@bp.route("/explain/<int:id>")
def render_explain(id):
    for exercise in exercises:
        if exercise.id == id:
            response = ChatBotAi.explain(exercise.question)
            return render_template("students/exercises/full.html", exercise=exercise, response=response)
    return render_template("students/exercises/full.html", exercise=exercise, response=None)
