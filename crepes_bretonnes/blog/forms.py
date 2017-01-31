from django import forms
from .models import Person

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100, required=True)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label="Enter your email adress", required=True)
	renvoi = forms.BooleanField(help_text="Cocher si vous souhaitez obtenir copie du mail",required=False)

#Recuperation du modele Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

#Form avec image
class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()

