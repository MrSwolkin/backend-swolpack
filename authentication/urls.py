from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("authentication/token", TokenObtainPairView.as_view(), name="token-obtain-view"),
    #path("authentication/token", obtain_auth_token, name="api_token_auth"),

]