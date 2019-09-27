from django.contrib import admin

# Register your models here.
from customer.models import *

class Cutomer_Admin(admin.ModelAdmin):
    list_display = ['id_publik','nama','email','ukuran_baju']

admin.site.register(Customer, Cutomer_Admin)
