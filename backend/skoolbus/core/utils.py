from django.forms import ValidationError
from rest_framework import serializers

from .enums import TransactionStatus
from .models import  SchoolProfile, Transactions
from django.db.models import Sum

uni = ('jd')
uniuyo_list = [
    'jude21w', 
    'jakewr4',
]
uniuyo_teachers_list = [ 
    'mma213',
    'egemba211'


]
unical_teachers_list = [ 

    'michr4',
    'alice454t'
]

unical_list = [
    'unique',
    'jennifer' 

]

uniuyo_details = {
    'name':'big Uniuyo',
    'rating':'200th position'
    }

unical_details = {
    'name':'big Unical',
    'rating':'300th position'
    }
    


def check_list(pin):
    if (pin in unical_list):
        return pin
        
    elif pin in uniuyo_list:
        return pin
        
    elif (pin in unical_list ):
        return pin
    
    elif (pin in unical_teachers_list ):
        return pin
        
    elif (pin  in uniuyo_teachers_list):
        return pin

    else:
        raise serializers.ValidationError({'details': 'incorrect pin, Try again'})
  


def get_balance(wallet):

    
    Transactions.objects.filter(
        wallet = wallet,
        transaction_status = TransactionStatus.SUCCESS

    ).aggregate(Sum('amount'))
