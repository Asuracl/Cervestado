from django.urls import path
#from .views import index,cervezas,registro
from .views import index, cervezas, registro, login

urlpatterns = [ 
    path('', index, name='index' ),
    path('cervezas/', cervezas, name='cervezas'),
    path('registro/', registro, name='registro'),
    path('login/', login, name='login')
    
]

