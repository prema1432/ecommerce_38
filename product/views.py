from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


# def index():
#     return "ju"


def products(request):
    return render(request, 'products.html')


def computer_products(request):
    return render(request, 'computer_products.html')
