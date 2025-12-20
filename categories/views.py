from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializer import CategorySerializer

class CategoryCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer