from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import FormView
from .forms import FileFieldForm

# Imaginary function to handle an uploaded file.
from .file_handler import handle_uploaded_file

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'img_processing/upload_image.html'  # Replace with your template.
    success_url = 'img_processing/uploaded_image.html'  # Replace with your URL or reverse().

    def get(self, request, *args, **kwargs):
        form = FileFieldForm()
        context = {'form': form}
        return render(request, 'img_processing/upload_image.html', context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        
        if form.is_valid():
            fs = FileSystemStorage()
            for f in files:              
                filename = fs.save(f.name, f)
                uploaded_file_url = fs.url(filename)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def index(request):
    return render(request, 'img_processing/index.html')

def uploaded_image(request):
    return render(request, 'img_processing/uploaded_image.html')

"""
def upload_image(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        return render(request, 'img_processing/uploaded_image.html')
    # 'uploaded_file_url': uploaded_file_url
    return render(request, 'img_processing/upload_image.html')
"""
