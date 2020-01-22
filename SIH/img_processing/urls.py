from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('upload_image', views.upload_image, name='upload_image'),
    # path('uploaded_image', views.uploaded_image, name='uploaded_image'),
    path('upload_image', views.FileFieldView.as_view(), name='upload_image')
]