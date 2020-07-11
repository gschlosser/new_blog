from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint, render_template, Markup, url_for


app = Flask(__name__)

posts = [
    {
        'author':'Gabe',
        'title': 'First post',
        'content': 'lalalalala',
        'date_posted': '30 June 2020'
    }
]

@app.route('/', methods=['GET'])
def homefunc():
    return render_template('home.html', posts=posts)

@app.route('/about')
def aboutpage():
    return render_template('about.html')


if __name__ == '__main__':
    app.run() #debug=True if you so