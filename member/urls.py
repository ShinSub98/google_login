from django.urls import path
from . import views
from .views import *

app_name = 'member'

urlpatterns = [
    path('google/', GoogleLoginApi.as_view()),
    path('login/', views.google_login)
]