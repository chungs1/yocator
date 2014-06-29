from app import db

YO_UNSUBSCRIBED = 0
YO_SUBSCRIBED = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    yo_name = db.Column(db.String(60), index=True, unique = True)
    timestamp = db.Column(db.DateTime)
    subscribed = db.Column(db.SmallInteger, default=YO_SUBSCRIBED)
    yo_count = db.Column(db.Integer)
    yos = db.relationship('Yo', backref='author', lazy='dynamic')

class Yo(db.Model):
    timestamp = db.Column(db.DateTime)
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subscriber_count = db.Column(db.Integer, default=0)
    yo_count = db.Column(db.Integer, default=0)
