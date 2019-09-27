from rest_framework import serializers
from customer.models import *
import datetime
from datetime import datetime , timedelta
from django.utils import timezone

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','id_publik',  'nama', 'email', 'ukuran_baju')
