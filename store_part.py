from flask import (Blueprint,
                   render_template,
                   session,
                   request,
                   redirect,
                   url_for)
from store_models import Item,Order,db
from cart import Cart
from store_lib import cart_work
from forms import OrderForm
from datetime import datetime
from mail_part import send_mail

store_app = Blueprint('store_app', __name__,
                        template_folder='templates')


@store_app.route("/")
def view_items():
    items = Item.query.all()
    return render_template("store/items.html",
                           items=items)


@store_app.route("/<int:item_number>")
def view_item(item_number):
    item = Item.query\
           .filter(Item.id==item_number)\
           .first()
    return render_template("store/item.html",
                           item=item)



@store_app.route("/add__to_cart/<int:item_number>")
def add_to_cart(item_number):
    item = Item.query.filter(Item.id==item_number).first()
    cart_work(session)
    if item:
        session["cart"].add_item(item)
        return redirect(url_for('store_app.view_cart'))
    return "Виникла помилка неіснуючий товар"



@store_app.route("/cart")
def view_cart():
    cart_work(session)
    cart = session.get("cart")
    return render_template("store/cart.html",
                           cart=cart)




@store_app.route("/create_order",methods=["GET","POST"])
def create_order():
    cart_work(session)
    cart = session.get("cart")
    if not cart.items:
        return "Товарів немає"
    
    if request.method == "POST":
        user_data = request.form
        order = Order(name=user_data.get("name"),
                      phone=user_data.get("phone"),
                      email=user_data.get("email"),
                      price=cart.get_price(),
                      date=datetime.now())
        for item in cart.items:
            order.items.append(item)
        send_mail("egen13@ukr.net",
                  "Замовлення в магазині",
                  order.get_data_to_message())
        db.session.add(order)
        db.session.commit()
        
        session.get("cart").clear()
        
        return render_template("store/thank.html")
            
    form = OrderForm()
    return render_template("store/order.html",
                            form=form,
                            cart=cart)


@store_app.route("/clean_cart")
def clean_cart():
    cart_work(session)
    cart = session.get('cart')
    cart.clear()
    return redirect(url_for('store_app.view_cart'))
