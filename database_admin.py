from app import app, db
from app.models import Stats, User, Yo

stats = Stats.query.first()
users = User.query.all()
yos = Yo.query.all()

def help():
    print("""
    stats.subscriber_count
    stats.yo_count
    
    User.id
    User.yo_name
    User.timestamp
    User.subscribed
    User.yo_count
    User.yos
    
    Yo.id
    Yo.timestamp
    Yo.user_id
    Yo.author
    """)
