from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .db import AbonneDb
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def crete_page_abo(request):

    return render(request, 'add_abonnes.html' , {"stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY, "title" : 'Abonnement'})
@login_required
def crete_abo(request , ty):
    data = {
        "type" : ty ,
        "user" : request.user.username ,
    }
    AbonneDb.createAbonnee(data)
    return HttpResponse("abonnee cree avec succces")

