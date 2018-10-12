from django.urls import path
from . import views

app_name="db"

urlpatterns = [
    path('login/', views.db_login),
    path('fuck/', views.fuck, name='fuck'),
    path('index01/', views.firstindex)

]