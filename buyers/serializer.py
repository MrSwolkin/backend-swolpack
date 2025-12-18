from rest_framework import serializers
from .models import Buyer

class BuyerSerialzer(serializers.ModelSerializer):
    
    class Meta: 
        model = Buyer
        fields = "__all__"