from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    reference = models.IntegerField(null=True) # champ optionnel avec null=True
    created_at = models.DateTimeField(auto_now_add=True) # date auto à la création
    available = models.BooleanField(default=True) 
    title = models.CharField(max_length=200)
    picture = models.URLField() # une chaîne de caractères qui sera de forme "URL"
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True) # relation many-to-many
    # Le paramètre related_name indique le nom à utiliser pour la relation inverse depuis l'objet lié vers celui-ci.

    def __str__(self):
        return self.title


class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE) # relation one-to-one
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE) # relation many-to-one

    def __str__(self):
        return self.contact.name