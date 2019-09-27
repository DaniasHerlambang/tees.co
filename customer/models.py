from __future__ import unicode_literals
from django.db import models
import uuid
import os
import ast
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import magic

# Create your models here.
class Customer(models.Model):
    id_publik =models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4)
    nama            = models.CharField(max_length=100, blank=True)
    email           = models.EmailField(blank=True)
    ukuran_baju     = models.PositiveSmallIntegerField(null= True, blank= True)

    def __str__(self):
        return "{0}: {1}".format(self.id , self.nama)

    class Meta :
        verbose_name_plural = 'Daftar Customer'
