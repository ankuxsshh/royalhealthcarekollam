from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('managements',views.managements,name="managements"),
    path('facilities',views.facilities,name="facilities"),
    path('departments',views.departments, name="departments"),
    path('contactus',views.contactus,name="contactus"),
    path('gallery',views.gallery,name="gallery"),
    path('services',views.services,name="services"),
    path('findadoctor',views.findadoctor,name="findadoctor")
]