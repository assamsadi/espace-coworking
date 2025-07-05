from django.shortcuts import render
from salle.db import SalleDb
from reservation.db import ReservationDb
from user.db import UserDb
from equipment.db import EquipmentDb
from service.db import ServiceDb
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required

def dashboard_page (request):
    data ={
        "all_salle" : SalleDb.count_all_salle(),
        "salle_libre" : SalleDb.count_salle_by_status("libre"),
        "salle_occupe" : SalleDb.count_salle_by_status("occupé"),
        "salle_reserver" : SalleDb.count_salle_by_status("reserver"),
        "all_reservation" : ReservationDb.count_all_resevation(),
        "resevationen_pas_encore" : ReservationDb.count_resevation_by_status("pas encore"),
        "resevationen_en_cours" : ReservationDb.count_resevation_by_status("préparation en cours"),
        "resevationen_Prêt" : ReservationDb.count_resevation_by_status("Prêt"),
        "staffs":  UserDb.filter_user({"username" : "", "role" : "staff"}),
        "all_equipment" : EquipmentDb.count_equipmnet(),
        "all_servise" : ServiceDb.count_service(),
        "title" : "Dashboard"
    }
    return render(request, 'dashboard.html' , data)
