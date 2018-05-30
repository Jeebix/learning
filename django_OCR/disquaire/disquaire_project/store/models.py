from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

class Album(models.Model):
    reference = models.IntegerField(null=True) # champ opptionnel avec null=True
    created_at = models.DateTimeField(auto_now_add=True) # date auto à la création
    available = models.BooleanField(default=True) 
    title = models.CharField(max_length=200)
    picture = models.URLField() # une chaîne de caractères qui sera de forme "URL"
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True) # relation many-to-many
    # Le paramètre related_name indique le nom à utiliser pour la relation inverse depuis l'objet lié vers celui-ci.


class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album) # relation one-to-one
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE) # relation many-to-one