from flask import (Blueprint,
                   redirect,
                   request,
                   render_template)
from mail_part import send_mail
from models import Message,db

connection_page = Blueprint('connection_page', __name__,
                        template_folder='templates')


@connection_page.route("/recieve",methods=["GET","POST"])
def recieve_message():
    if request.method == "POST":
        form_data = request.form
        send_mail("egen13@ukr.net",
                  f"Лист від - {form_data.get('name')} {form_data.get('email')}",
                  f"Саме повідомлення - {form_data.get('message')}")
        message = Message(name=form_data.get('name'),
                          email=form_data.get('email'),
                          text=form_data.get('message'))
        db.session.add(message)
        db.session.commit()
    return render_template("blog/thank.html")


