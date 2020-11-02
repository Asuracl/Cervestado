from django.urls import path
from . import views

app_name='main'

urlpatterns = [ 
    path('', views.landingPage, name='landingPage' ),
    path('index', views.index, name='index' ),
    path('cervezas.html/', views.cervezas, name='cervezas'),
    path('registro.html/', views.registro, name='registro')
]

