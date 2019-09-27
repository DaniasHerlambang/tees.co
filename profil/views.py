from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Sum
import datetime

from profil.models import *
from . import serializers
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

class ProfilView(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     content = {'message': 'Hello, World!'}
    #     return Response(content)

    def get(self, request, format=None):
        profils = Profil.objects.all()
        print(profils)
        serializer = serializers.ProfilSerializer(profils, many=True)
        results = {'records': str(len(profils)),
                   'rows': serializer.data}
        return Response(results)


    @transaction.atomic
    def post(self, request, format=None):
        serializer = serializers.ProfilSerializer(data=request.data)
        if serializer.is_valid():
            t = Profil()
            t.nama_lengkap =  request.data['nama_lengkap']
            t.telp =  request.data['telp']
            t.email =  request.data['email']
            t.alamat =  request.data['alamat']
            t.foto =  request.data['foto']
            t.save()

            return Response( {'message': 'User Baru Berhasil Dibuat'})
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def put(self, request, pk):
        saved_profil = get_object_or_404(Profil.objects.all(), id_publik=pk)
        serializer = serializers.ProfilSerializer(instance=saved_profil, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response({"success": "Profil '{}' updated successfully".format(saved_profil.nama_lengkap)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        # Get object with this pk
        profil = get_object_or_404(Profil.objects.all(), id_publik=pk)
        profil.delete()
        return Response({"message": "Profil with id `{}` has been deleted.".format(pk)})
