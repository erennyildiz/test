from django.shortcuts import render
from app.serializers import *
from app.models import *
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

class customer(views.APIView):
    def post(self, request, format=None):
        many = True if isinstance(request.data, list) else False
        serializer = CustomerSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response("customer created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

class account(views.APIView):
    def post(self, request, format=None):
        many = True if isinstance(request.data, list) else False
        serializer = AccountSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response("account created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

class transfer(views.APIView):
    def post(self, request, format=None):
        many = True if isinstance(request.data, list) else False
        serializer = TransferSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response("transfer created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, format=None):
        transfer = Transfer.objects.all()
        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data)

class transferHistory(views.APIView):
    def get(self, request, from_accountid, format=None):
        filtered_from_account = Account.objects.filter(pk = from_accountid).first()
        transfer = Transfer.objects.filter(from_account = filtered_from_account)
        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data)
