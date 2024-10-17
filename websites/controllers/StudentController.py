from flask import Blueprint, render_template, request

from websites.models.TeachersModel import students
from websites.tools.chatBot.chatbot import ChatBotAi

bp = Blueprint('students', __name__, url_prefix='/students/')


@bp.route('/')
def renderHome():
    return render_template("students/home.html", students=students)


@bp.route('/chatBot', methods=["GET"])
def renderChatBot(response=None):
    return render_template("students/chatBot.html", response=response)


@bp.route('/chatBot', methods=["POST"])
def chatBot(response=None):
    question = request.form.get('question')
    response = ChatBotAi.test_chat(question)
    return render_template("students/chatBot.html", response=response)
