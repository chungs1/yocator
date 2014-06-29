from app import db
import datetime


YO_UNSUBSCRIBED = 0
YO_SUBSCRIBED = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    yo_name = db.Column(db.String(60), index=True, unique = True)
    subscribed = db.Column(db.SmallInteger, default=YO_SUBSCRIBED)
    yo_count = db.Column(db.Integer)

class Yo(db.Model):
    id = db.Column(db.Integer, primary_key = True)

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subscriber_count = db.Column(db.Integer)
    yo_count = db.Column(db.Integer)

