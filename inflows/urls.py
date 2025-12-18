from django.urls import path
from . import views

urlpatterns = [
    path("inflows/", views.InflowCreateListView.as_view(), name="inflow-create-list"),
    path("inflows/<int:pk>/", views.InflowRetrieveUpdateDestroyView.as_view(),
        name="inflow-details-list")
]