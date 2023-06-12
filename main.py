from flask import Flask
from models import Article,MenuElement,SocialNetwork,Message,User
from models import db
from blog_part import blog_app
from dotenv import load_dotenv
import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from connection_part import connection_page
from mail_part import send_mail,mail
from admin_adapter import ImageView,AdminView
from auth_part import auth_app
from auth_elements import login_manager
from portfolio_part import portfolio_app
from store_models import Item,Order,StoreMenuElement
from store_part import store_app
from flask_session import Session
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__,
             static_url_path='')

app.config.update(
    MAIL_SERVER=os.environ["MAIL_SERVER"],
    MAIL_PORT=os.environ["MAIL_PORT"],
    MAIL_USE_SSL=os.environ["USE_SSL"],
    MAIL_USERNAME = os.environ["MAIL_USERNAME"],
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
)
mail.init_app(app)
login_manager.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.secret_key = os.environ["SECRET_KEY"]
db.init_app(app)

app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]
Session(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    app.jinja_env.globals["menu_elements"] = MenuElement.query.all()
    app.jinja_env.globals["socials"] = SocialNetwork.query.all()
    app.jinja_env.globals["store_menu_elements"] = StoreMenuElement.query.all()


app.register_blueprint(blog_app,
                       url_prefix='/blog')

app.register_blueprint(connection_page)

app.register_blueprint(auth_app,
                       url_prefix='/auth')

app.register_blueprint(portfolio_app)

app.register_blueprint(store_app,
                       url_prefix='/store')


admin = Admin(app, name='САЙТ', template_mode='bootstrap3')
admin.add_view(ImageView(Article, db.session))
admin.add_view(AdminView(MenuElement, db.session))
admin.add_view(AdminView(SocialNetwork, db.session))
admin.add_view(AdminView(Message, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(ImageView(Item, db.session))
admin.add_view(AdminView(Order, db.session))
admin.add_view(AdminView(StoreMenuElement, db.session))



if __name__ == "__main__":
    app.run()
