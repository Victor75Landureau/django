from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.core.files import File
from datetime import datetime 
from .forms import MiniURLForm
from mini_url.models import MiniURL

def liste(request):
    """ Affichage des redirections """
    minis = MiniURL.objects.order_by('-nb_acces')

    return render(request, 'mini_url/liste.html', locals())

def nouveau(request):
	""" Affichage du formulaire pour créer un url """
	if request.method == "POST":	
		form = MiniURLForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(liste)
	else:
		form = MiniURLForm()
	return render(request, 'mini_url/nouveau.html', {'form': form})

def redirection(request, code):
    """ Redirection vers l'URL enregistrée """
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_acces += 1
    mini.save()
    return redirect(mini.url, permanent=True)
