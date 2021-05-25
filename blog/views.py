from django.shortcuts import render
from .models import Post

# Create your views here.
def view_posts(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,'blog/all_posts.html',context)