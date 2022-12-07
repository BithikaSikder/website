from django.shortcuts import render, HttpResponse
from myapp.models import customer, Contact, proimage

# Create your views here.
def home(request):
    # return HttpResponse('This is Home Page')
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method=="POST":
        cp_name = request.POST["cp_name"]
        cp_phone = request.POST["cp_phone"]
        cp_email = request.POST["cp_email"]
        cp_msg = request.POST["cp_msg"]
    
        cont = Contact(cp_name=cp_name, cp_phone=cp_phone, cp_email=cp_email, cp_msg=cp_msg)
        cont.save()
    return render(request, 'contact.html')


def customers(request):
    all_customers = customer.objects.all
    return render(request, 'customer_details.html', {'all':all_customers})

def products(request):
    all_products = proimage.objects.all
    return render(request, 'products.html', {'all':all_products})
