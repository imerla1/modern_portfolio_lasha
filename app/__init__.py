from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title='Homepage')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/work')
def work():
    return render_template('work.html')


app.run(debug=True)
