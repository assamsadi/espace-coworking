import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, "home.html", {
        "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY
    })

@csrf_exempt
def create_checkout_session(request  , id):
    if request.method == 'POST':
        
        data = request.body
        
        print(f"Received price: {int(data)}")
        c= int(data)
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
               'price_data': {
                        'currency': 'mad',  
                        
                        'product_data': {
                            'name': 'la reservation les salle',
                        },
                        'unit_amount': c,  
                    },
                    'quantity': 1,
            }],
            mode='payment',
            success_url=f'http://localhost:8000/e1/{id}',
            cancel_url='http://localhost:8000/cancel/',
        )
        return JsonResponse({'id': session.id})

def success(request):
    return render(request, "success.html")

def cancel(request):
    return render(request, "cancel.html")

def create_checkout_abonne(request ):
    if request.method == 'POST':
        
        data = request.body
        
        print(f"Received price: {int(data)}")
        c= int(data)
        
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
               'price_data': {
                        'currency': 'mad',  
                        
                        'product_data': {
                            'name': 'abonnement',
                        },
                        'unit_amount': c,  
                    },
                    'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/abonnes/create/pro',
            cancel_url='http://localhost:8000/cancel/',
        )
        return JsonResponse({'id': session.id})
