from flask import Flask, render_template, url_for, request, redirect
from students import Students
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

students_list = []


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/students', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_student = Students(request.form['first_name'], request.form['last_name'])
        students_list.append(new_student)
        return redirect(url_for('index'))
    return render_template('index.html', students=students_list)


@app.route('/students/new')
def new():
    return render_template('new.html')


@app.route('/students/<int:id>', methods=['GET','PATCH', 'DELETE'])
def find(id):
    student = [student for student in students_list if student.id == id][0]
    if request.method == b'PATCH':
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        students_list.remove(student)
        return redirect(url_for('index'))
    return render_template('find.html', student=student)


@app.route('/students/<int:id>/edit')
def edit_user(id):
    student = [student for student in students_list if student.id == id][0]
    return render_template('edit.html', student=student)


if __name__ == "__main__":
    app.run(debug=True)
