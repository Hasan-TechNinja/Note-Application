from django import forms 

class calculator(forms.Form):
    num1 = forms.CharField(label="First Number", required=False)
    num2 = forms.CharField(label="Last Number")
    