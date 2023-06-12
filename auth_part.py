from flask import Blueprint, render_template, abort,request,redirect
from auth_elements import login_manager
from flask_login import login_user
from models import User
from forms import UserForm

auth_app = Blueprint('auth_app', __name__,
                        template_folder='templates')


@auth_app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        user = User.query.filter(User.username == form_data.get("username") \
                                 and User.password == form_data.get("password")).first()
                           
        if user:
            login_user(user)
            return redirect("/admin")
        
    form = UserForm()
    return render_template("auth/login.html",
                           form=form)
