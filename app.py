from flask import Flask, render_template

app = Flask(__name__)


# Home page route
@app.route('/')
def index():
    return 'Hello, Dexter! This is an updated Flask app.'


# New Route: Services page
@app.route('/services')
def services():
    return render_template('services.html')


# Updated About page route
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')


# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html', email='lian@ryan.com')


if __name__ == '__main__':
    app.run(debug=True)
