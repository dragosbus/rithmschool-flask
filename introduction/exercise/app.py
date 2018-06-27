from flask import Flask, render_template, request, url_for
from snacks import Snacks


app = Flask(__name__)

snacks_list = [Snacks('hamburger', 'bh')]


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        new_snack = Snacks(request.form['name'], request.form['kind'])
        snacks_list.append(new_snack)
    return render_template('index.html', snacks=snacks_list)


@app.route('/show/<int:id>')
def show(id):
    snack = [snack for snack in snacks_list if snack.id == id][0]
    return render_template('show.html', snack=snack)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/show/<int:id>/edit')
def edit(id):
    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
