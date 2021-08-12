from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/success/<name>/<age>')
def success(name, age):
    return 'Welcome {} with Age: {}...!!!'.format(name, age)


@app.route('/login', methods=['POST'])
def login():
    user_name = request.form['name']
    age = request.form['age']
    return redirect(url_for('success', name=user_name, age=age))


@app.route('/user/<name>')
def general_user(name):
    return "Hello User: {}".format(name)


@app.route('/admin')
def admin():
    return "Hello Admin"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
