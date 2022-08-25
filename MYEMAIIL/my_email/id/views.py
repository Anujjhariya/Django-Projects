from contextlib import redirect_stdout
from email import message
from importlib.metadata import requires
# from ssl import _PasswordType
# from xml.sax import make_parser
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from id.models import Persone


# Create your views here.
# def index(request):
#     return HttpResponse("hello")

def index(request):
    return render(request,'id/home.html',context={})

def form_data(request):
    if request.method=='POST':
        First_name = request.POST['first_name']
        Last_name = request.POST['Last_name']
        Company_name = request.POST['Company_name']
        Contact_number = request.POST['Contact_number']
        Email = request.POST['Email']
        Password = make_password(request.POST)
        if Persone.objects.filter(Contact_number = Contact_number).exists:
            message.error(request,"Phone number already exist")
        elif Persone.objects.filter(Email = Email).exists:
            message.error(request,"Email already exist")
        else:
            Persone.objects.create(First_name=First_name,
                                   Last_name=Last_name,
                                   Company_name=Company_name,
                                   Contact_number=Contact_number,
                                   Email=Email,
                                   Password=Password,)

            return redirect('/')