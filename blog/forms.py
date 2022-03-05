from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    dep =forms.CharField(max_length=200)
    p_no =forms.CharField(max_length=10)
