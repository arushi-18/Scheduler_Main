from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns=[
	path('all_posts/<str:username>',views.view_MyPosts,name="all-posts"),
	path('',views.PostListView.as_view(),name="all-posts"),
	path('posts/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
	path('posts/new_post',views.PostCreateView.as_view(),name="post-create"),
	path('posts/<int:pk>/update/',views.PostUpdateView.as_view(),name="post-update"),
	path('posts/<int:pk>/delete/',views.PostDeleteView.as_view(),name="post-delete"),
]