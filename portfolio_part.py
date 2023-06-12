from flask import Blueprint, render_template

portfolio_app = Blueprint('portfolio_app', __name__,
                        template_folder='templates')

@portfolio_app.route("/")
def index():
    return render_template("main_page/index.html")
