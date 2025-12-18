from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("authentication/token", TokenObtainPairView.as_view(), name="token-obtain-view"),
    path("authentication/token/refresh/", TokenRefreshView.as_view(),
        name="token_refresh"),
    path("authentication/token/verify/",
        TokenVerifyView.as_view(), name="token_verify"),
    #path("authentication/token", obtain_auth_token, name="api_token_auth"),

]