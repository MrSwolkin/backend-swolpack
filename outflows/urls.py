from django.urls import path
from . import views

urlpatterns = [
    path("outflows/", views.OuflowsCreateListView.as_view(), name="ouflow-create-list"),
    path("outflows/<int:pk>", views.OuflowsretrieveUpdateDestroyView.as_view(),
        name="ouflow-details-list"),
]