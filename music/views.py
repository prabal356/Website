from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album
from django.template import loader
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')    #django is set up to look into a directory named template thats why we do not write template/muic/...
    context = {'all_albums': all_albums}
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")