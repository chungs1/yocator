from app import app
from flask import render_template, flash, request
from app import app, db
from config import API_TOKEN
import models
import datetime
import requests
import random


@app.route('/')
@app.route('/index')
def index():
    stats = models.Stats.query.first()
    total_subs = stats.subscriber_count
    total_yos = stats.yo_count

    return render_template("index.html", subscribers=total_subs, yos=total_yos)

@app.route('/subs')
def subs():
    stats = models.Stats.query.first()
    total_subs = stats.subscriber_count
    total_yos = stats.yo_count

    return render_template("subs.html", subscribers=total_subs, yos=total_yos)


@app.route('/add/')
def add():
    """
    get stats
    make a new yo
    increment number of subscirbers
    increment the number of yos
        for the user as well

    """
    new_subscriber_name = request.args.get('username')
    stats_object = models.Stats.query.first()
    subscriber = models.User.query.filter_by(yo_name=new_subscriber_name).first()

    if not subscriber:
        subscriber = models.User(yo_name=new_subscriber_name, 
                timestamp=datetime.datetime.utcnow(), yo_count=0)
        stats_object.subscriber_count += 1

    new_yo = models.Yo(timestamp=datetime.datetime.utcnow(), author=subscriber)
    subscriber.yo_count += 1
    stats_object.yo_count += 1
    db.session.add(new_yo)
    db.session.add(stats_object)
    db.session.add(subscriber)
    db.session.commit()
    
    stats = models.Stats.query.first()
    total_subs = stats.subscriber_count
    total_yos = stats.yo_count

    return render_template("index.html", subscribers=total_subs, yos=total_yos)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/subscriber_count')
def subscriber_count():
    stat = models.Stats.query.first()
    return str(stat.subscriber_count+500)

@app.route('/yo_count')
def yo_count():
    stat = models.Stats.query.first()
    return str(stat.yo_count+1500)

