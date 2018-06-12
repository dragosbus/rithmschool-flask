from flask import Flask, render_template, url_for, request, redirect
from Users import Users

users = []

app = Flask(__name__)

@app.route('/')
def main_page():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_user = Users(request.form['first_name'], request.form['last_name'])
        users.append(new_user)
        return redirect(url_for('index'))
    return render_template('index.html', users=users)

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)