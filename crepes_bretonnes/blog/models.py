from django.db import models

class Article(models.Model):
   titre = models.CharField(max_length=100)
   slug = models.SlugField(max_length=100)
   auteur = models.CharField(max_length=42)
   contenu = models.TextField(null=True)
   date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                               verbose_name="Date de parution")
   categorie = models.ForeignKey('Categorie')
   def __str__(self):
        return self.titre

class Person(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=42)
    def __str__(self):
        return self.prenom

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="./media/image/")
    def __str__(self):
           return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom

class Moteur(models.Model):
    nom = models.CharField(max_length=25)
    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur)
    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre')
    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit)
    vendeur = models.ForeignKey(Vendeur)
    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)