
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
## Create your views here.


#def index(request):
#   template = loader.get_template('main/index.html')
#    context = {}
#    return HttpResponse(template.render(context, request))
#
#def cervezas(request):
#    template = loader.get_template('main/cervezas.html')
#    context = {}
#    return HttpResponse(template.render(context, request))
#
#def registro(request):
#    template = loader.get_template('main/registro.html')
#    context ={}
#    return HttpResponse(template.render(context, request))

#---------------
#from django.shortcuts import render, redirect
#from django.contrib.auth import logout as do_logout
#from django.contrib.auth import authenticate
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login as do_login
#from django.contrib.auth.forms import UserCreationForm
#
## Create your views here.
#
#def index(request):
#    return render (request, 'main/index.html')
#
#
#def cervezas(request):
#    return render (request, 'main/cervezas.html')
#
#def quienesomos(request):
#    return render (request, 'main/quienesomos.html')
#
#def registro(request):
#    return render (request, 'main/registro.html')
#
#def inicio(request):
#    return render (request, 'main/index.html')
#
#def register(request):
#    # Creamos el formulario de autenticación vacío
#    form = UserCreationForm()
#    if request.method == "POST":
#        # Añadimos los datos recibidos al formulario
#        form = UserCreationForm(data=request.POST)
#        # Si el formulario es válido...
#        if form.is_valid():
#
#            # Creamos la nueva cuenta de usuario
#            user = form.save()
#
#            # Si el usuario se crea correctamente 
#            if user is not None:
#                # Hacemos el login manualmente
#                do_login(request, user)
#                # Y le redireccionamos a la portada
#                return redirect('/')
#    # Si queremos borramos los campos de ayuda
#    form.fields['username'].help_text = None
#    form.fields['password1'].help_text = None
#    form.fields['password2'].help_text = None        
#
#    # Si llegamos al final renderizamos el formulario
#    return render(request, "main/register.html", {'form': form})
#
#def login(request):
#    # Creamos el formulario de autenticación vacío
#    form = AuthenticationForm()
#    if request.method == "POST":
#        # Añadimos los datos recibidos al formulario
#        form = AuthenticationForm(data=request.POST)
#        # Si el formulario es válido...
#        if form.is_valid():
#            # Recuperamos las credenciales validadas
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password']
#
#            # Verificamos las credenciales del usuario
#            user = authenticate(username=username, password=password)
#
#            # Si existe un usuario con ese nombre y contraseña
#            if user is not None:
#                # Hacemos el login manualmente
#                do_login(request, user)
#                # Y le redireccionamos a la portada
#                return redirect('/')
#
#    # Si llegamos al final renderizamos el formulario
#    return render(request, "main/login.html", {'form': form})
#
#def logout(request):
#    # Finaliza la sesion
#    do_logout(request)
#    # Redireccion a login
#    return redirect('/')    

from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def cervezas(request):
    return render(request, 'main/cervezas.html')


def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None        

    # Si llegamos al final renderizamos el formulario
    return render(request, "main/registro.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "main/login.html", {'form': form})

def logout(request):
    # Finaliza la sesion
    do_logout(request)
    # Redireccion a login
    return redirect('/')    













