from rest_framework import generics

from .models import Inflow
from .serializer import InflowSerializer

class InflowCreateListView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer

class InflowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer