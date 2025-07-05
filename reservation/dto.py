from datetime import datetime
from salle.db import SalleDb
def validation_time(request , id):
    msg_error = {}
    if request.POST["date_debut"] == "" or request.POST["date_fin"] == "":
        msg_error["time"] = "Veuillez renseigner les champs date début et date fin"
    date_debut = datetime.strptime(request.POST["date_debut"] , '%Y-%m-%dT%H:%M')
    date_fin = datetime.strptime(request.POST["date_fin"], '%Y-%m-%dT%H:%M')
    if date_debut >= date_fin:
        msg_error["time"] = "la date non valide"
    if not SalleDb.valisation_time({"form" :request.POST["date_debut"]  , "to": request.POST["date_fin"] } , id) :
        msg_error["time"] = "la salle occupé"
    return  msg_error
