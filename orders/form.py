from django import forms
from .models import OrderInfo

class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['address','city','email','full_name',]
