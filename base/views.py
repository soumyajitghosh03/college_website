from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def academics(request):
    return render(request, 'academics.html')

def campus(request):
    return render(request, 'campus.html')

def hostel(request):
    return render(request, 'hostel.html')

def admission(request):
    return render(request, 'admission.html')

def faculty(request):
    return render(request, 'faculty.html')

def contact(request):
    return render(request, 'demo.html')

def feedback(request):
    return render(request, 'feedback.html')