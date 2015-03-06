from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hel')
def hello_world():
    return 'Hello World!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/programs')
def programs():
    return render_template('programs.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
