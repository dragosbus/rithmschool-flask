from flask import Flask, render_template, url_for, request, redirect
import psycopg2
    


def create_user(f_name, l_name):
    con = psycopg2.connect(database='flaskfundamentals')
    cur = con.cursor()
    cur.execute('''INSERT INTO users(first_name, last_name) VALUES(%s, %s)''', (f_name, l_name))
    con.commit()
    cur.close()
    con.close()

def read_users():
    con = psycopg2.connect(database='flaskfundamentals')
    cur = con.cursor()
    cur.execute('''SELECT * FROM users''')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

    return res

app = Flask(__name__)

@app.route('/')
def main_page():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        create_user(first_name, last_name)
        
        return redirect(url_for('index'))
    return render_template('index.html', users=[])

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/find', methods=['GET','POST'])
def find():
    found = None
    if request.method == 'POST':
        try:
            search_id = request.form['search_id']
            found = read_users()[int(search_id)]
        except:
            redirect(url_for('index'))
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