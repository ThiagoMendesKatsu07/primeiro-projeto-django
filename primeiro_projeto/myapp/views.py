from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def gastronomia(request):
    return render(request,'index2.html')

def pontos(request):
    return render(request,'index3.html')

