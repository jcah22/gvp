from django.shortcuts import render

# Create your views here.
def monitoreo(request):
    return render(request,'monitoreo/monitoreo.html')

def detalles(request):
    return render(request,'monitoreo/detalles.html')