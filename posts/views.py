from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm

from django.utils.text import slugify



class ListView(View):
	def get(self,request):
		template_name = 'lista.html'
		posts = Post.objects.all().order_by('titulo')
		compa = {
		'posts':posts,
		}
		return render(request,template_name,compa)

class DetailView(View):
	def get(self,request,slug):
		template_name = 'detalle.html'
		post = Post.objects.get(slug=slug)
		context = {
		'post':post
		}
		return render(request,template_name,context)

class UpdateView(View):
	def get(self,request):
		template_name = 'nuevo.html'
		form = PostForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST)
		new_post = form.save(commit=False)
		new_post.slug = slugify(new_post.titulo)
		new_post.save()
		return redirect('lista')










