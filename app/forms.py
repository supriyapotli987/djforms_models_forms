from django import forms


class Studentform(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sid=forms.IntegerField()
    Semail=forms.EmailField()