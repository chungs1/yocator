from app import db

YO_UNSUBSCRIBED = 0
YO_SUBSCRIBED = 1

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    yo_name = db.Column(db.String(60), index=True, unique = True)
    subscribed = db.Column(db.SmallInteger, default=YO_SUBSCRIBED)


