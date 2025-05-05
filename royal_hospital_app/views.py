from django.shortcuts import render
from .models import Testimonial

# Create your views here.


def index(request):
    testimonials = Testimonial.objects.order_by('-created_at')
    return render(request, 'index.html', {'testimonials': testimonials})

def about(request):
    return render(request, 'about.html')

def departments(request):
    return render(request, 'departments.html')

def contactus(request):
    return render(request, 'contactus.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')

def findadoctor(request):
    return render(request, 'findadoctor.html')

def facilities(request):
    return render(request, 'facilities.html')

def managements(request):
    return render(request, 'managements.html')

def careers(request):
    return render(request, 'careers.html')

def intpatient(request):
    return render(request, 'intpatient.html')

def events(request):
    return render(request, 'events.html')

