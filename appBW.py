# pip3 install psycopg2-binary
# pip3 install flask-sqlalchemy
# in ipython EVERY TIME: from sqlalchemy.sql import text


from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///movies_example'
app.app_context().push()


db = SQLAlchemy()
db.app = app
db.init_app(app)


app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug= DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')
