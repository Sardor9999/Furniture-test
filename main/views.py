from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request=request, template_name="main/index.html")

def about(request):
    return render(request=request, template_name="main/about.html")

def shop(request):
    return render(request=request, template_name="main/shop.html")
def furniture(request):
    return render(request=request, template_name="main/furniture.html")
def contact(request):
    return render(request=request, template_name="main/contact.html")