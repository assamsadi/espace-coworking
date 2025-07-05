from django.shortcuts import redirect, render
from reservation.db import ReservationDb
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required

def list_page(request):
    role = request.user.role
    data =  {
             "num_salle" : request.POST.get('num_salle' , ''),
             "status" : request.POST.get('status' , ''),
        }
    print(data)
    return render( request, "list_salle_staff.html" , {"products" : ReservationDb.filter(data , role) ,"title" : "Reservations"})
@login_required
def to_preparation(request , id):
    a= ReservationDb.updateStatus(id , "préparation en cours")
    print(f"ddddddddddddddddddd{a}")
    return redirect("list_page_staff")
@login_required
def to_prete( request , id):
    ReservationDb.updateStatus(id , "Prêt")
    return redirect("list_page_staff")

    

