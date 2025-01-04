from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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
