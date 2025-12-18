from django.urls import path
from . import views

urlpatterns = [
    path("buyers/", views.BuyerCreateListView.as_view(), name='buyers-create-list'),
    path("buyers/<int:pk>/", views.BuyerRetrieveUpdateDestroyView.as_view(),
        name='buyers-details-list'),
]