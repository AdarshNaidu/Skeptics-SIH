from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Imaginary function to handle an uploaded file.
from .file_handler import handle_uploaded_file

def index(request):
    return render(request, 'img_processing/index.html')

def uploaded_image(request):
    return render(request, 'img_processing/uploaded_image.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'img_processing/uploaded_image.html')
    # 'uploaded_file_url': uploaded_file_url
    return render(request, 'img_processing/upload_image.html')

