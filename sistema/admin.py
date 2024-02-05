from django.contrib import admin

# Register your models here.

from .models import Auto, Propietario, CustomUser

admin.site.register(Auto)
admin.site.register(Propietario)
admin.site.register(CustomUser)


