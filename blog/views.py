from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def view_MyPosts(request,username):
	user_list=Post.objects.filter(author__username=username)#author_id=id)
	page = request.GET.get('page', 1)
	paginator = Paginator(user_list,5)
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		posts=paginator.page(1)
	except EmptyPage:
		posts=paginator.page(paginator.num_pages)
	context={
		'posts':posts,
		'name':username
	}
	return render(request,'blog/all_posts.html',context)

class PostListView(ListView):
	model=Post
	template_name='index.html' #<app>/<model>_<viewtype>.html
	context_object_name='posts'
	ordering=['-date_posted']
	paginate_by=5

class PostDetailView(DetailView):
	model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','subtitle','content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','subtitle','content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False