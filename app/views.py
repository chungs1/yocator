from app import app
from flask import render_template, flash, request
from app import app, db
from config import API_TOKEN
import models
import requests
import random


@app.route('/')
@app.route('/index')
def index():
    stats = models.Stats.query.get(0)
    total_subs = stats.subscriber_count
    total_yos = stats.yo_count

    return render_template("index.html", subscribers=total_subs, yos=total_yos)

@app.route('/add/?username=<new_subscriber_name>', methods=['GET', 'POST'])
def add(new_subscriber_name):
    """
    get stats
    make a new yo
    increment number of subscirbers
    increment the number of yos
        for the user as well

    """
    stats_object = models.Stats.query.get(0)
    subscriber = models.Users.query.filter_by(yo_name=new_subscriber_name).first()

    if not subscriber:
        subscriber = new models.User(name=new_subscriber_name, yo_count=0)
        stats_object.subscriber_count += 1

    new_yo = models.Yo(user=subscriber)
    subscriber.yo_count += 1
    stats_object.yo_count += 1
    db.session.add(new_yo)
    db.session.add(stats_object)
    db.session.add(subscriber)
    db.session.commit()
    
    #YO EVERYONE
    send_yo()

def send_yo():

    if random.randint(0,100) == 95:j
        requests.post("http://api.justyo.co/yoall/", data={'api_token': API_TOKEN})


