from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from datetime import datetime 

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    if int(id_article) == 100:
    	return redirect(view_redirection)

    return HttpResponse('<h1>Mon article {0} ici</h1>'.format(id_article))

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)  
)

def view_redirection(request):
	return redirect('afficher_article', id_article=42)

def date_actuelle(request):
	return render(request, 'blog/date.html', {"date": datetime.now()})

def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())