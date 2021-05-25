from django.urls import path
from . import views

urlpatterns=[
	path('all_posts/',views.view_posts,name="all-posts")
]