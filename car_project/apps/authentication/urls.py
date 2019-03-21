from django.urls import path

from .views import  RegistrationApiView, LoginApiView

app_name = 'authentication'
urlpatterns = [
    path('user/', RegistrationApiView.as_view()),
    path('user/login/', LoginApiView.as_view())
]
