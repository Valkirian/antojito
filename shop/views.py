from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Salchipapa, Empanada, ArepadeHuevo, Carimanola, Bollo
from django.http import JsonResponse
from . import send_whataspp
import datetime
# Create your views here.


def home(request):
    return render(request, 'shop/home.html')


@login_required
def ppage(request):
    if request.method == 'GET':
        salchipapas = Salchipapa.objects.all()
        empanadas = Empanada.objects.all()
        arepasdehuevo = ArepadeHuevo.objects.all()
        carimanolas = Carimanola.objects.all()
        bollos = Bollo.objects.all()
        return render(request, 'shop/princitalpage.html', {"salchipapas": salchipapas, "empanadas": empanadas, "arepasdehuevo": arepasdehuevo, "carimanolas": carimanolas, "bollos": bollos})
    else:
        pass


@login_required
def payment(request):
    salchipapas = Salchipapa.objects.all()
    empanadas = Empanada.objects.all()
    arepasdehuevo = ArepadeHuevo.objects.all()
    carimanolas = Carimanola.objects.all()
    bollos = Bollo.objects.all()
    if request.method == 'GET':
        return render(request, 'shop/payment.html', {"salchipapas": salchipapas, "empanadas": empanadas, "arepasdehuevo": arepasdehuevo, "carimanolas": carimanolas, "bollos": bollos})
    elif request.method == "POST":
        producto = request.POST['productos']
        cantidad = request.POST['cuenta']
        mensaje = ""
        if cantidad == "":
            mensaje = "No se selecciono una cantidad"
        else:
            mensaje = f"Pedido creado exitosamente"
        mensaje_confirm = f"Se creo el pedido con {cantidad} unidades del producto {producto}"
        username = request.user.username
        try:
            whatsapp_body = f"El usuario {username} realizo un pedido con {cantidad} unidades del producto {producto} en la fecha {datetime.date.today()}"
            send_whataspp.SendWhatsapp(whatsapp_body)
            return render(request, 'shop/payment.html', {"cantidad": cantidad, "producto": producto, "confirm": mensaje_confirm, "mensaje": mensaje, "salchipapas": salchipapas, "empanadas": empanadas, "arepasdehuevo": arepasdehuevo, "carimanolas": carimanolas, "bollos": bollos})
        except:
            error = "No se creo el pedido correctamente!"
            return render(request, 'shop/payment.html', {"error": error, "salchipapas": salchipapas, "empanadas": empanadas, "arepasdehuevo": arepasdehuevo, "carimanolas": carimanolas, "bollos": bollos})
    else:
        pass


def singup(request):
    if request.method == 'GET':
        return render(request, 'shop/singup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Create a new User
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password2'])
                user.save()
                django_login(request, user)
                return redirect('shop:ppage')
            except IntegrityError:
                return render(request, 'shop/singup.html', {'form': UserCreationForm(), 'error': 'The username has already been taken. Plese chose a new username'})
        else:
            return render(request, 'shop/singup.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'shop/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            django_login(request, user)
            return redirect('shop:ppage')


@login_required
def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('shop:home')
