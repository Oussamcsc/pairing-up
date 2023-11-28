from flask import Flask, render_template

app = Flask(__name__)


# Home page route
@app.route('/')
def index():
    return 'Hello, Dexter! This is a Flask app.'


# About page route
@app.route('/about')
def about():
    return render_template('about.html')


# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
