from models import db 

item_order_table = db.Table('item_order_table',
                            db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
                            db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
                            )

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    creator = db.Column(db.String(300))
    img = db.Column(db.String(250))

    def __str__(self):
        return self.name

    def get_date_to_message(self):
        message = f"""Назва товару - {self.name}
Ціна товару - {self.price}
Виробник товару - {self.creator}"""
        return message


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    phone = db.Column(db.String(30))
    email = db.Column(db.String(250))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    items = db.relationship("Item",
                            secondary=item_order_table)

    def get_data_to_message(self):
        message = f"""Ім'я - {self.name}
телефон замовника - {self.phone}
емейл - {self.email}
Ціна замовлення - {self.price}
Дата замовлення - {self.date}"""
        message += f"\n{'-'*40}\n"
        for item in self.items:
            message += item.get_date_to_message()
            message += f"\n{'-'*40}\n"
        return message


class StoreMenuElement(db.Model):
    __tablename__ = "store_elements"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    link = db.Column(db.String(250))
        


