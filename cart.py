class Cart:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        if item.id not in [item.id for item in self.items]:
            self.items.append(item)

    def items_count(self):
        return len(self.items)

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price

    def clear(self):
        self.items = []




