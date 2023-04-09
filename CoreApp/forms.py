from django.forms import ModelForm

from CoreApp.models import Order


class CreateOrder(ModelForm):
    class Meta:
        model = Order
        exclude = ["updated_at", "created_at", "tracking_id"]
