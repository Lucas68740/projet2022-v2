from django.shortcuts import render, HttpResponseRedirect
from .forms import TelForm
from . import models

def bonjour(request):
    return render(request,"monappli/bonjour.html")


# Create your views here.

def ajout(request):
    if request.method == "POST":
        form = TelForm(request)
        return render(request,"monappli/ajout.html",{"form" : form,"id":form.id})
    else:
        form = TelForm()
        return render(request, "monappli/ajout.html",{"form" : form,})

def traitement(request):
    lform = TelForm(request.POST)
    if lform.is_valid():
        tel = lform.save()
        return HttpResponseRedirect("/monappli")
    else :
        return render(request, "monappli/ajout.html", {"form": lform})

def index(request):
    liste = models.Tel.objects.all()
    return render(request,"monappli/index.html",{"liste": liste})

def affiche(request, id):
    tel = models.Tel.objects.get( pk = id )
    return render(request,"monappli/affiche.html",{"tel": tel})

def update(request, id):
    tel = models.Tel.objects.get( pk = id )
    form = TelForm(tel.dico())
    return render(request,"monappli/ajout.html",{"form":form, "id": id})

def updatetraitement(request):
    lform = TelForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect("/monappli/")
    else:
        return render(request, "monappli/affiche.html", {"form": lform})

def delete(request, id):
    tel = models.Tel.objects.get( pk = id )
    tel.delete()
    return HttpResponseRedirect("/monappli/")




