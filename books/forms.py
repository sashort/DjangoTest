from django import forms

class BasicForm(froms.Form):
    you_name = forms.CharField(label='Your Name', max_length=100)