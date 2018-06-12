from flask import Flask, render_template, url_for, request, redirect
from Users import Users

u1 = Users('dragos', 'busuioc')
users = [u1]

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

@app.route('/find', methods=['GET','POST'])
def find():
    found = None
    if request.method == 'POST':
        search_id = request.form['search_id']
        found = [user for user in users if user.id == int(search_id)][0]
    return render_template('find.html', user=found)

@app.route('/edit', methods=['GET','POST'])
def edit():
    found = None
    if request.method == 'POST':
        try:
            search_id = request.form['useredit-id']
            found = [user for user in users if user.id == int(search_id)][0]
        except:
            return redirect(url_for('index'))

        if request.args.get('new_first_name'):
            new_first_name = request.form['new_first_name']
            found.f_name = new_first_name

        if request.args.get('new_last_name'):
            new_last_name = request.form['new_last_name']
            found.l_name = new_last_name

        return redirect(url_for('index'))
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)