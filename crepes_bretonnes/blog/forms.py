from django import forms

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100, required=True)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label="Enter your email adress", required=True)
	renvoi = forms.BooleanField(help_text="Cocher si vous souhaitez obtenir copie du mail",required=False)