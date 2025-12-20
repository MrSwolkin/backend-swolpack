from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Buyer
from .serializer import BuyerSerialzer


class BuyerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerialzer


class BuyerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerialzer