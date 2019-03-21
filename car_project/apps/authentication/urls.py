from django.urls import path

from .views import  RegistrationApiView, LoginApiView, UserReceiveUpdateView

app_name = 'authentication'
urlpatterns = [
    path('user/', UserReceiveUpdateView.as_view()),
    path('users/', RegistrationApiView.as_view()),
    path('users/login/', LoginApiView.as_view())
]
