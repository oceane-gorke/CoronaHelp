from django import forms
from appone.models import Habitant
from appone.models import Collectivite

class Identification(forms.Form):
    email = forms.EmailField(label='Votre email',max_length=50)
    mdp = forms.CharField(label='Votre mot de passe',max_length=50,widget=forms.PasswordInput)

class IndentificationForm(forms.ModelForm):
    class Meta:
        model = Habitant
        fields = [
            'email',
            'mdp'
        ]
    widgets = {
        'mdp': forms.PasswordInput()
    }

class IdentificationC(forms.Form):
    ville = forms.CharField(label='Votre ville',max_length=50)
    mdp = forms.CharField(label='Votre mot de passe',max_length=50,widget=forms.PasswordInput)

class IndentificationFormC(forms.ModelForm):
    class Meta:
        model = Collectivite
        fields = [
            'ville',
            'mdp'
        ]
    widgets = {
        'mdp': forms.PasswordInput()
    }