from rest_framework import generics

from .models import Buyer
from .serializer import BuyerSerialzer


class BuyerCreateListView(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerialzer


class BuyerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerialzer