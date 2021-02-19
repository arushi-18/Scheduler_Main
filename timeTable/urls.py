from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.table_home,name="table-home")
]