from django.urls import path

from .views import  RegistrationView

app_name = 'authentication'
urlpatterns = [
    path('user/', RegistrationView.as_view())
]
