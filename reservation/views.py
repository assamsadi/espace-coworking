import datetime
import json
from django.shortcuts import render , redirect
from salle.db  import SalleDb
from equipment.db  import EquipmentDb
from service.db  import ServiceDb
from .db  import ReservationDb
import qrcode
import base64
from io import BytesIO
import os
from django.utils import timezone
from datetime import datetime
from billet.db import BilletDb
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from datetime import datetime
from django.contrib.auth.decorators import login_required
from workspace import context_processors
from . import dto
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class ReservationViews:
    salles=[]
    equipments = []
    services = [] # add not yet
    equipments_reserve = []
    services_reserve = [] # add not yet
    salle_reserve= None
    to_d = None
    from_d = None
    duree = None
    id_billet = None
    id_r= None
    set_navigation = "menu"
    prix = 0
    prix_salle = 0
    prix_equipments = 0
    prix_service = 0
    prix_reserve = 0
    s= 0
    error = {}
    time= {}
    context={}

    
    @staticmethod
    @login_required
    def create_page(  request):
       
        print( type(context_processors.is_abonnee(request)["is_abonnee"]))
        data =  {
             "name" : request.POST.get('name' , ''),
             "categorie" : request.POST.get('categorie' , ''),
        }
        ReservationViews.salles = SalleDb.filter(data)
        ReservationViews.equipments = EquipmentDb.get_all_equipment()
        ReservationViews.services = ServiceDb.get_all_equipment()
        data= {
        "salles" : ReservationViews.salles,
        "equipments" : ReservationViews.equipments,
        "services" : ReservationViews.services,
        "equipments_reserve" : ReservationViews.equipments_reserve,
        "services_reserve" : ReservationViews.services_reserve,
        "salle_reserve" : ReservationViews.salle_reserve,
        "duree" : ReservationViews.duree,
        "set_navigation" : ReservationViews.set_navigation,
        "prix_salle" : ReservationViews.prix_salle,
        "prix" : round(int(ReservationViews.prix), 2),
        "prix_equipments" : ReservationViews.prix_equipments,
        "prix_service" : ReservationViews.prix_service,
        "tva" : ReservationViews.prix*0.38,
        "total" : round(  ReservationViews.prix*1.38, 2),
        "s": ReservationViews.s,
        "input_form" :ReservationViews.from_d,
        "input_to" :ReservationViews.to_d,
        "error" : ReservationViews.error,
         "title" : 'New_Reservation'
        }
        return render(request,'add_reservation.html' , data)
    


#----------------- equipment --------------------------------#

    #add equipment 
    @staticmethod
    @login_required
    def add_equipment(request , id ):

        equipment= EquipmentDb.get_equipment(id)
        equi= request.POST["equi"]
        date_equi = {"id" : equipment.id ,  "name" :equipment.nom , "que" : int (equi) , "prix" :equipment.prix ,  "prixTotale" : float(equipment.prix)* int(equi) }
        ReservationViews.equipments_reserve.append(date_equi)
        ReservationViews.prix=  ReservationViews.prix +  float(equipment.prix)* int(equi)
        ReservationViews.prix_equipments =    ReservationViews.prix_equipments +  float(equipment.prix)* int(equi)
        if context_processors.is_abonnee(request)["is_abonnee"]:
            ReservationViews.prix_equipments = 0
            ReservationViews.prix = 0
 
        return redirect("create_page")


    #delete equipment
    @staticmethod
    @login_required
    def delete_equipment(request , i):
        index  = int(i) - 1
        equipment =  ReservationViews.equipments_reserve[index]
        ReservationViews.prix=  ReservationViews.prix- equipment['prixTotale']
        ReservationViews.prix_equipments=  ReservationViews.prix_equipments- equipment['prixTotale']
        if context_processors.is_abonnee(request)["is_abonnee"]:
            ReservationViews.prix_equipments = 0
            ReservationViews.prix = 0
        del ReservationViews.equipments_reserve[index]
        return redirect("create_page")


#----------------- service --------------------------------#

    #add service 
    @staticmethod
    @login_required
    def add_service(request , id):
        service= ServiceDb.get_equipment(id)
       
        date_equi = { "id":service.id  , "name" :service.nom   , "prix" :service.prix ,  "prixTotale" : float(service.prix)}
        ReservationViews.services_reserve.append(date_equi)
        ReservationViews.prix=  ReservationViews.prix +  float(service.prix)
        ReservationViews.prix_service =    ReservationViews.prix_service +  float(service.prix)
        if context_processors.is_abonnee(request)["is_abonnee"]:
            ReservationViews.prix_service = 0
            ReservationViews.prix = 0
        return redirect("create_page")

    #delete equipment
    @staticmethod
    @login_required
    def delete_service(request , i):
        index  = int(i) - 1
        service =  ReservationViews.services_reserve[index]
        ReservationViews.prix=  ReservationViews.prix- service['prixTotale']
        ReservationViews.prix_reserve=  ReservationViews.prix_reserve- service['prixTotale']
        if context_processors.is_abonnee(request)["is_abonnee"]:
            ReservationViews.prix_service = 0
            ReservationViews.prix = 0
        del ReservationViews.services_reserve[index]
        return redirect("create_page")
    
#----------------- select salle --------------------------------#
    def select_salle(request, id):
        salle = SalleDb.get_salle(id)
        # ReservationViews.prix =  ReservationViews.prix +
        ReservationViews.prix_salle = salle.prix
        ReservationViews.prix = salle.prix
        ReservationViews.salle_reserve = salle

        if context_processors.is_abonnee(request)["is_abonnee"]:
            ReservationViews.prix_salle = 0
            ReservationViews.prix = 0

# ---------------- - clalcul duree -------------------------------- #
# AHLI LHAWA
    @staticmethod
    @login_required
    def calcul_duree(request):
        print(f'duuuuuuuuuuuuu { ReservationViews.salle_reserve.id}')
        ReservationViews.from_d = request.POST["date_debut"] 
        ReservationViews.to_d = request.POST["date_fin"]
        date_debut = datetime.strptime(request.POST["date_debut"] , '%Y-%m-%dT%H:%M')
        date_fin = datetime.strptime(request.POST["date_fin"], '%Y-%m-%dT%H:%M')
        ReservationViews.duree = date_fin - date_debut
        ReservationViews.prix_salle = int( ReservationViews.duree.days)* float(ReservationViews.salle_reserve.prix)
        ReservationViews.prix = int( ReservationViews.duree.days)* float(ReservationViews.salle_reserve.prix)  + ReservationViews.prix
        ReservationViews.time={"form" :request.POST["date_debut"]  , "to": request.POST["date_fin"] }
        if context_processors.is_abonnee(request)["is_abonnee"]:
            ReservationViews.prix_salle = 0
            ReservationViews.prix = 0

        return ReservationViews.duree
    

# --------------------- navigation -------------------------------#

    #menu
    @staticmethod
    @login_required
    def go_to_menu(request):
        ReservationViews.insanitation()
        ReservationViews.set_navigation ="menu"
        return redirect("create_page")

    
    #timing
    @staticmethod
    @login_required
    def go_to_time(request , id ):
        ReservationViews.select_salle(request,id)
        ReservationViews.set_navigation ="timeing"
        return redirect("create_page")
    
    #service_equipment
    @staticmethod
    @login_required
    def go_to_service_equipment(request  ):
        ReservationViews.error = dto.validation_time(request ,ReservationViews.salle_reserve.id)
        if  ReservationViews.error  :
            return redirect("create_page")
        ReservationViews.calcul_duree(request)
        ReservationViews.s= 1
        print(request)
        return redirect("create_page")
    
    @staticmethod
    @login_required
    def go_to_timezone(request  ):
      
        ReservationViews.s= 0
        print(request)
  
        return redirect("create_page")


    #facture 
    @staticmethod
    @login_required
    def go_to_facture(request):
        ReservationViews.set_navigation ="facture"
        return redirect("create_page")
    

#------------------insanitation------------------- #
    def insanitation():
        ReservationViews.salles=[]
        ReservationViews.equipments = []
        ReservationViews.services = [] # add not yet
        ReservationViews.equipments_reserve = []
        ReservationViews.services_reserve = [] # add not yet
        ReservationViews.salle_reserve= None
        ReservationViews.to_d = None
        ReservationViews.from_d = None
        ReservationViews.duree = None
        ReservationViews.id_billet = None
        ReservationViews.id_r= None
        ReservationViews.set_navigation = "menu"
        ReservationViews.prix = 0
        ReservationViews.prix_salle = 0
        ReservationViews.prix_equipments = 0
        ReservationViews.prix_service = 0
        ReservationViews.prix_reserve = 0
        ReservationViews.s= 0
        ReservationViews.error = None





#----------------------- billet ---------------------- #
    @staticmethod
    @login_required
    def updoade_billet (request): 
        idR =  ReservationViews.save(request)
        # 1. Générer le QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f"http://127.0.0.1:8000/equipment/{ReservationViews.id_r}/"
        qr.add_data(qr_data)
        
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # 2. Convertir QR code en base64
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()

        # 3. Contexte pour le template
        if context_processors.is_abonnee(request)["is_abonnee"]:
            qr_code= ""
        context = {
            "user": request.user.username,
            "salles" : ReservationViews.salles,
            "equipments" : ReservationViews.equipments,
            "services" : ReservationViews.services,
            "equipments_reserve" : ReservationViews.equipments_reserve,
            "services_reserve" : ReservationViews.services_reserve,
            "salle_reserve" : ReservationViews.salle_reserve,
            "duree" : ReservationViews.duree.days,
            "set_navigation" : ReservationViews.set_navigation,
            "prix_salle" : ReservationViews.prix_salle,
            "prix" : round(int(ReservationViews.prix), 2) ,
            "prix_equipments" : ReservationViews.prix_equipments,
            "prix_reserve" : ReservationViews.prix_reserve,
            "tva" : ReservationViews.prix*0.38,
            "total" : round(  ReservationViews.prix*1.38, 2),
            "qr_code": qr_code,
            "num_salle": ReservationViews.salle_reserve.name,
            "duee" : ReservationViews.duree.days,
            "current_time": timezone.now().date()

}
        ReservationViews.context = context

        # insert billet_new
        deta = {
        'user': request.user.username,
        'from_reserve': ReservationViews.from_d,
        'to_reserve': ReservationViews.to_d,
        'duree':int( ReservationViews.duree.days),
        'num_salle': ReservationViews.salle_reserve.name,
        'qr_code': qr_code,  # This was missing
        'equipements': json.dumps(ReservationViews.equipments_reserve ),
        'servises': json.dumps(ReservationViews.services_reserve ),
        'prix': round(int(ReservationViews.prix), 2) ,
        'status': "not pay",
        "type" : "norme"

        }

        billet = BilletDb.createBillet(deta)
        ReservationViews.id_billet = billet.id
        ReservationDb.changeNum_ticket(ReservationViews.id_r ,billet.id)
        # 4. Rendu HTML
        template = get_template('billet.html')
        html = template.render(context)

        # 5. Générer PDF
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

        if not pdf.err:
            # 6. Sauvegarde sur le disque
            save_dir = os.path.join(settings.BASE_DIR, "pdfs")
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, "report_with_qr.pdf")

            with open(file_path, "wb") as f:
                f.write(result.getvalue())

            # 7. Téléchargement par l'utilisateur
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report_with_qr.pdf"'
            ReservationViews.insanitation()
            return render( request, "donebi.html" )

        return HttpResponse("Erreur lors de la génération du PDF", status=500)
    @staticmethod
    @login_required
    def upi(request):
        template = get_template('billet.html')
        html = template.render(ReservationViews.context)

        # 5. Générer PDF
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

        if not pdf.err:
            # 6. Sauvegarde sur le disque
            save_dir = os.path.join(settings.BASE_DIR, "pdfs")
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, "report_with_qr.pdf")

            with open(file_path, "wb") as f:
                f.write(result.getvalue())

            # 7. Téléchargement par l'utilisateur
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report_with_qr.pdf"'
            return  response

        return HttpResponse("Erreur lors de la génération du PDF", status=500)

#-------------------- SAEVE -------------------------------#
    def save(request):
        print(ReservationViews.salle_reserve)
        ty = ""
        if context_processors.is_abonnee(request)["is_abonnee"]:
            ty = "pro"
        else:
            ty = "normal"
        date = {
        'user': request.user.username,
        'from_reserve':datetime.strptime(ReservationViews.from_d, '%Y-%m-%dT%H:%M').date(),
        'to_reserve': datetime.strptime( ReservationViews.to_d , '%Y-%m-%dT%H:%M').date(),
        'duree': int( ReservationViews.duree.days),
        'num_salle': ReservationViews.salle_reserve.name,
        'num_ticket': "",  # This was missing
        'equipements': json.dumps(ReservationViews.equipments_reserve ),
        'servises': json.dumps(ReservationViews.services_reserve ),
        'prix':  round(int(ReservationViews.prix), 2)  ,
        'status': "pas encore",
        "type" : ty,
        "date" : timezone.now().date()
        }
        SalleDb.time_includ(ReservationViews.time, ReservationViews.salle_reserve.id)
        SalleDb.change_status(ReservationViews.salle_reserve.name , "reserver")
        ReservationViews.id_r= ReservationDb.createRsevation(date).id

    
#------------------- list --------------------------#
    @staticmethod
    @login_required
    def list_reservation(request):
        role = request.user.username
        data =  {
             "num_salle" : request.POST.get('num_salle' , ''),
             "status" : request.POST.get('status' , ''),
        }
        print(data)
        return render( request, "list_reservation.html" , {"products" : ReservationDb.filterByUser(data , role) ,"title" : "Reservations"})



