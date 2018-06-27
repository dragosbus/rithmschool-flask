from flask import Flask, render_template, request, url_for
from snacks import Snacks


app = Flask(__name__)

snacks_list = [Snacks('hamburger', 'bh')]

@app.route('/')
def root():
    return render_template('index.html', snacks=snacks_list)


@app.route('/show/<int:id>')
def show(id):
    snack = [snack for snack in snacks_list if snack.id == id][0]
    return render_template('show.html', snack=snack)


if __name__ == '__main__':
    app.run(debug=True)
