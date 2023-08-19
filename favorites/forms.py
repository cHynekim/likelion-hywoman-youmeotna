from django import forms

class UpdateQuantityForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    new_quantity = forms.IntegerField(min_value=0)