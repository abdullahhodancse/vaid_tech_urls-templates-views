from django.shortcuts import render
from app1.models.fileUp_model import UploadFfiles

def pdf_cart_view(request):
    # সব ইউজারের PDF ফাইল দেখাবে
    pdf_files = UploadFfiles.objects.filter(file__iendswith='.pdf')
    
    return render(request, 'file_load.html', {'pdf_files': pdf_files})
