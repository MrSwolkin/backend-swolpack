from rest_framework import generics

from .models import Outflow
from .serializer import OutflowSerializer

class OuflowsCreateListView(generics.ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

class OuflowsretrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
