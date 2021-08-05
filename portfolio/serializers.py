from rest_framework import serializers
from .models import Customer, Investment, Stock


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

        fields = ('pk', 'name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')


class InvestmentSerializer(serializers.ModelSerializer):
    cust_name = serializers.CharField(read_only=True, source="customer.name")

    class Meta:
        model = Investment
        fields = (
            'pk', 'customer', 'cust_number', 'cust_name', 'category', 'description', 'acquired_value', 'acquired_date',
            'recent_value',
            'recent_date')


class StockSerializer(serializers.ModelSerializer):
    cust_name = serializers.CharField(read_only=True, source="customer.name")
    class Meta:
        model = Stock
        fields = ('pk', 'customer', 'cust_number', 'cust_name', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')
