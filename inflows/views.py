from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Inflow
from .serializer import InflowSerializer

class InflowCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer

class InflowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer