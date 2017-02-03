from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.core.files import File
from datetime import datetime 
from blog.models import Article, Contact
from .forms import ContactForm, PersonForm

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    couleurs = {'FF0000':'rouge', 
            'ED7F10':'orange', 
            'FFFF00':'jaune', 
            '00FF00':'vert', 
            '0000FF':'bleu', 
            '4B0082':'indigo', 
            '660099':'violet'}
    return render(request, 'blog/color.html', locals())

def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html', {'contacts': contacts})

def contact(request):
	# Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        url = form.cleaned_data['url à reduire']
        pseudo = form.cleaned_data['pseudo']
        envoi = True
    # Quoiqu'il arrive, on affiche la page du formulaire.
    #Pour plus de filtre sur les formulaires cf openclassroom
    return render(request, 'blog/contact.html', locals())

def person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid(): 
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
    return render(request, 'blog/person.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'contact.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})


def page(request):
	return render(request, 'blog/mapage.html')

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    if int(id_article) == 100:
    	return redirect(view_redirection)

    return render(request, 'blog/article.html', locals())
    """return HttpResponse('<h1>Mon article {0} ici</h1>'.format(id_article))"""

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