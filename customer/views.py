from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Sum
import datetime

from customer.models import *
from . import serializers
from django.db import transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        customers = Customer.objects.all()
        print(customers)
        serializer = serializers.CustomerSerializer(customers, many=True)
        results = {'records': str(len(customers)),
                   'rows': serializer.data}
        return Response(results)

    @transaction.atomic
    def post(self, request, format=None):
        serializer = serializers.CustomerSerializer(data=request.data)
        if serializer.is_valid():
            t = Customer()
            t.nama =  request.data['nama']
            t.email =  request.data['email']
            t.ukuran_baju =  request.data['ukuran_baju']
            t.save()

            return Response( {'message': 'Customer Baru Berhasil Dibuat'})
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def put(self, request, pk):
        saved_customer = get_object_or_404(Customer.objects.all(), id_publik=pk)
        serializer = serializers.CustomerSerializer(instance=saved_customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response({"success": "Customer '{}' updated successfully".format(saved_customer.nama)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        customer = get_object_or_404(Customer.objects.all(), id_publik=pk)
        customer.delete()
        return Response({"message": "Customer with id `{}` has been deleted.".format(pk)})
