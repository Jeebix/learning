# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Album, Artist, Booking, Contact

def index(request):
    # request albums
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)



def search(request):
    # L'objet request est une instance de la classe WSGIRequest qui a des propriétés comme GET
    # qui renvoie un dictionnaire contenant les arguments passés à l'URL
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

    # Chercher à travers les relations d'un album :
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    if not albums.exists():
        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    else:
        albums = ["<li>{}</li>".format(album['name']) for album in albums]
        message = """
            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            <ul>
                {}
            </ul>
        """.format("</li><li>".join(albums))

    return HttpResponse(message)
    
