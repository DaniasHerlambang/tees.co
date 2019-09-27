from rest_framework import serializers
from profil.models import *
import datetime
from datetime import datetime , timedelta
from django.utils import timezone

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ('id','id_publik',  'nama_lengkap', 'telp', 'email', 'alamat', 'foto')

# find . -path '*/migrations/__init__.py' -exec truncate -s 0 {} + -o -path '*/migrations/*' -delete
# find . -path '*/__pycache__/__init__.py' -exec truncate -s 0 {} + -o -path '*/__pycache__/*' -delete
