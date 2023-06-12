from wtforms_alchemy import ModelForm
from models import User
from store_models import Order

class UserForm(ModelForm):
    class Meta:
        model = User


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['price','date']
    
