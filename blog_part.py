from flask import Blueprint,render_template
from models import Article

blog_app = Blueprint('blog_app', __name__,
                        template_folder='templates')


@blog_app.route("/")
def get_articles():
    articles = Article.query.all()
    return render_template("blog/articles.html",articles=articles)

@blog_app.route("/<int:article_number>")
def view_article(article_number):
    article = Article.query.filter(Article.id==article_number).first()
    return render_template("blog/article.html",article=article)
