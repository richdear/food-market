from django import forms


class ItemForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    price = forms.FloatField(label='Price')
    description = forms.CharField(label='Description', max_length=200)
    image_url = forms.CharField(label='Image url', max_length=500)
