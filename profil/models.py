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


TIPE_REKENING = (
    (0, 'Sukarela'),
    (1, 'Deposit'),
)

KELAMIN = (
    (0, 'Wanita'),
    (1, 'Pria'),
)

# VALIDATION FILE AND FORMAT
def validate_file_type(value):
    ext = '%s' % os.path.splitext(value.name)[-1]
    if ext.lower() not in settings.PHOTO_EXTENSIONS:
        message = _('Invalid format, please choose: %(ext)s') % {'ext': settings.PHOTO_EXTENSIONS}
        raise ValidationError(message)
        print ('a')

    # Make uploaded file accessible for analysis by saving in tmp
    tmp_path = '%s' % os.path.splitext(value.name)[-1]
    default_storage.save(tmp_path, ContentFile(value.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    # Get MIME type of file using python-magic and then delete
    file_type = magic.from_file(full_tmp_path, mime=True)
    # print (file_type)
    default_storage.delete(tmp_path)
    # Raise validation error if uploaded file is not an acceptable form of media
    if file_type not in settings.PHOTO_CONTENT_TYPES:
        raise ValidationError('File type not supported. PNG/JPG recommended.')
        print ('b')
        # End Validation

class Tanggal(models.Model):
    tgl_dibuat = models.DateField(auto_now_add=True)
    tgl_update = models.DateField(auto_now=True)

    class Meta:
        abstract = True

def file_photo(instance, filename):
    return 'foto/{0}'.format( filename)

# Create your models here.
class Profil(Tanggal):
    id_publik =models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4)
    nama_lengkap = models.CharField(max_length=100, blank=True)  # Nama Lengkap Sesuai Identitas
    telp = models.CharField(max_length=20, blank=True)  # Telp/HP
    email = models.EmailField(blank=True, unique=True)
    alamat = models.CharField(max_length=50, blank=True)
    foto= models.FileField(_('arsip file'), upload_to=file_photo,
        validators=[validate_file_type], blank=True , max_length=300)

    def __str__(self):
        return "{0}".format( self.nama_lengkap)

    class Meta :
        unique_together = ['email']
        verbose_name_plural = 'Daftar Profil'
