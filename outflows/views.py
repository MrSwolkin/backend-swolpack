from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Outflow
from .serializer import OutflowSerializer

class OuflowsCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

class OuflowsretrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
