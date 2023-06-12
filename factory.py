from main import app
from models import db
from models import User


users = [{"username":"admin",
          "password":"123123"},
         {"username":"admin2",
          "password":"321321"}]

def create_users():
    if not User.query.all():
        for user in users:
            new_user = User(username=user['username'],
                            password=user['password'])
            db.session.add(new_user)
        db.session.commit()

with app.app_context():
    create_users()
