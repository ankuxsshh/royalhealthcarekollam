from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('managements',views.managements,name="managements"),
    path('facilities',views.facilities,name="facilities"),
    path('departments',views.departments, name="departments"),
    path('contactus',views.contactus,name="contactus"),
    path('gallery',views.gallery,name="gallery"),
    path('careers',views.careers,name="careers"),
    path('career-application/', views.career_application, name='career_application'),
    path('services',views.services,name="services"),
    path('findadoctor',views.findadoctor,name="findadoctor"),
    path('intpatient',views.intpatient,name="intpatient"),
    path('events',views.events,name="events"),
    path('appointment',views.appointment,name="appointment"),
    path('make-appointment/', views.make_appointment, name='make_appointment'),
]