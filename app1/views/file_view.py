from django.shortcuts import render
from app1.models.fileUp_model import UploadFfiles
from django.db.models import Count

def pdf_cart_view(request):
    
    pdf_files = UploadFfiles.objects.filter(file__iendswith='.pdf')
    user_file_count = UploadFfiles.objects.values('user__username') \
        .annotate(count=Count('id')) \
        .order_by('-count')  
    
    return render(request, 'file_load.html', {'pdf_files': pdf_files,'user_file_count': user_file_count})
