import os

from flask import Flask, render_template
from controllers.TeachersController import bp as teachers_bp
from controllers.ExerciseController import bp as exercise_bp
from controllers.StudentController import bp as students_bp
from controllers.DoExerciseController import bp as do_exercise_bp

app = Flask(__name__)

app.register_blueprint(teachers_bp)
app.register_blueprint(exercise_bp)
app.register_blueprint(students_bp)
app.register_blueprint(do_exercise_bp)

app.secret_key = 'mE_mAy_bEo_vAi'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
