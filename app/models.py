from app import db

YO_UNSUBSCRIBED = 0
YO_SUBSCRIBED = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    yo_name = db.Column(db.String(60), index=True, unique = True)
    subscribed = db.Column(db.SmallInteger, default=YO_SUBSCRIBED)
    timestamp = Column(DateTime, nullable=False, server_default=func.now())
    yo_count = db.Column(db.Integer)
    db.relationship('Alert', backref='user', lazy = 'dynamic')

class Yo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = Column(DateTime, nullable=False, server_default=func.now())
    user = db.Column(db.Integer, db.ForeignKey('user.id')

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subscriber_count = db.Column(db.Integer)
    yo_count = db.Column(db.Integer)

