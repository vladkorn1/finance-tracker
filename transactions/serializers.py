from rest_framework import serializers
from .models import Category, Transaction, Goal



class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Category
        fields = ('name', 'user')
    


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Transaction
        fields = ('category', 'user', 'type_of_transaction', 'amount', 'date', 'description')

    

class GoalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Goal
        fields = ('name', 'user', 'target_amount', 'current_amount', 'deadline')


