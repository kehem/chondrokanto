from django import forms
from .models import *



class infoForm(forms.ModelForm):
    class Meta:
        model = info
        fields = '__all__'

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'

class albumForm(forms.ModelForm):
    class Meta:
        model = album
        fields = '__all__'

class videoForm(forms.ModelForm):
    class Meta:
        model = video
        fields = '__all__'

class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'
        