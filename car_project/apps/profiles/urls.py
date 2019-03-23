from django.urls import path
from .views import ProfileRetrieveView

app_name = 'profiles'
urlpatterns = [
    path('profile/<str:username>', ProfileRetrieveView.as_view())
]
