from django.contrib import admin

# Register your models here.
from profil.models import *

class Profil_Admin(admin.ModelAdmin):
    list_display = ['id_publik','nama_lengkap','telp','email']

admin.site.register(Profil, Profil_Admin)
