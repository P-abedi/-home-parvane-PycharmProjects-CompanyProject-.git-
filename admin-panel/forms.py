from django import forms
from . import models

class ProductForm(forms.Form):
    class Meta:
        model = models.Product
        fields = '__all__'


class UserForm(forms.Form):
    class Meta:
        model = models.User
        fields = '__all__'