def validator(request , up):
    msg_errors= {}
    if request.POST["name"] =="" :
        msg_errors["name"]="Name is required"
    if request.POST["description"] =="" :
        msg_errors["description"]="Description is required"
    if request.POST["prix"] =="" :
        msg_errors["prix"]="Prix is required"
    if request.FILES.get('photo')==None and not up :
        msg_errors["photo"]="Photo is required"
    if request.POST["categorie"] =="" :
        msg_errors["categorie"]="categorie is required"
    
    return msg_errors
