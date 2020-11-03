from django.contrib import admin
from .models import Cerveza, User

# Register your models here.

admin.site.register(User)
admin.site.register(Cerveza)
