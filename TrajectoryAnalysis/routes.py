import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, Response, abort
from flaskblog.forms import *
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt, mail
from flask_login import login_user, logout_user, current_user, login_required
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Message

@app.route('/home/')
@app.route('/')
@login_required
def home():
    return render_template('home.html')