from app.models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('id', 'name')

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id', 'money_on_account', 'customer')

class TransferSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transfer
		fields = ('id', 'amount', 'from_account', 'to_account', 'from_account_new_amount', 'to_account_new_amount')