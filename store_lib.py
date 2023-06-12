from cart import Cart


def cart_work(session):
    if not session.get("cart"):
        session["cart"] = Cart()
