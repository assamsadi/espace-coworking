from io import BytesIO
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .db import BilletDb
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required

def list_page_billet(request):
    return render(request, 'list_billet.html' , { 'billets' : BilletDb.listBillet(request.user.username) , "title" : 'Billes'})
@login_required

def upload_pdf(request , id ):
        template = get_template('billet1.html')
        data = {'billet': BilletDb.getBillet(id)}
        html = template.render(data)

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
            return response
