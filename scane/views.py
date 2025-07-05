import datetime
from io import BytesIO

from datetime import datetime

from django.conf import settings
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from reservation.db import ReservationDb
from salle.db import SalleDb

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

class CardView():
    reservation = -1
    reservation_obj = -1
    prix = 0
    prix_services =  0 
    prix_equipment =  0 
    prix_tva =  0 
    prix_salle =  0 
    context= {}
    id = 0
    @staticmethod
    @login_required
    
    def qr_page(request, id):
        CardView.reservation = id
        return render(request, 'card.html', {'reservation': ReservationDb.getReservation(id) ,"stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY, "id": id})
    
    
    def calcule(request , id):
        reservation = ReservationDb.getReservation( id) 
        CardView.reservation_obj = ReservationDb.getReservation( id) 
        CardView.prix = reservation.prix
        for service in reservation.servises:
            CardView.prix_services = CardView.prix_services + int(service['prixTotale'])
        for equipment in reservation.equipements:
            CardView.prix_equipment +=  int (equipment['prixTotale'])
        CardView.prix_salle = int(int(SalleDb.get_salle_by_name(  reservation.num_salle ).prix)  * int(reservation.duree) ) 
        CardView.prix = reservation.prix
        CardView.prix_tva = (int(CardView.prix_services) +int(CardView.prix_equipment) + int(CardView.prix_salle)) * 0.38





    @staticmethod
    @login_required
    
    def up_up(request):
        ReservationDb.updatePiament(CardView.id, "avec succes")
        template_path = get_template('bb.html')
        # Create a Django response with the PDF as the attachment
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="facture.pdf"'
        template = get_template('bb.html')
        html = template.render( CardView.context )
        # create a PDF
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show the error page
        if not pisa_status.err:
             return response

    @staticmethod
    @login_required
    
    def uploud_pdf(request ,id):
        CardView.calcule(request , id)
        template_path = get_template('bb.html')
        CardView.id = id
        data={
            'reservation_obj':CardView.reservation_obj,
            'prix': CardView.prix ,
            "user" : request.user.username,
            'to':CardView.prix_services + CardView.prix_equipment + CardView.prix_salle,
            "current_date" : datetime.now().date() ,
            'prix_services': CardView.prix_services ,
            'prix_equipment': CardView.prix_equipment ,
            'prix_tva': CardView.prix_tva ,
            'prix_salle': CardView.prix_salle ,
        }
        CardView.context = data

        # Create a Django response with the PDF as the attachment
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="facture.pdf"'
        template = get_template('bb.html')
        html = template.render(data)
        # create a PDF
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show the error page
        if not pisa_status.err:
             return render(request, 'done.html' )
        
    @staticmethod
    @login_required
    
    def to_reserve(requst , id):
        salle= SalleDb.change_status(id , "occupé")
        return render( requst,"donefin.html")
    
    @staticmethod
    @login_required
    
    def to_done(requst , id):
        salle= SalleDb.change_status(id , "libre")
        return render( requst,"donefin.html")
    @staticmethod
    @login_required
    
    def done(requst):
        return render( requst,"done.html")
    @staticmethod
    @login_required
    
    def card_done(requst):
        return render( requst,"donefin.html")
        
