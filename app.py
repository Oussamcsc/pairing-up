from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Dexter! This is a Flask app.'


@app.route('/about')
def about():
    return render_template('about.html')



# New route: Contact page
@app.route('/contact')
def contact():
    return 'Contact us at lian1c@alma.edu'


if __name__ == '__main__':
    app.run(debug=True)
