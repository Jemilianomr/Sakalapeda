from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Categoria
from .forms import PostForm, CommForm

from django.utils.text import slugify

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class ListView(View):
	def get(self,request,cat=None):
		template_name = 'lista.html'
		categoria = None
		if cat:
			categoria = Categoria.objects.get(nombre=cat)
			posts = categoria.categorias.all()
		else:	
			posts = Post.objects.all().order_by('titulo')
		compa = {
			'posts':posts,
			'categoria':categoria,
			}
		return render(request,template_name,compa)

class DetailView(View):
	def get(self,request,slug):
		template_name = 'detalle.html'
		post = Post.objects.get(slug=slug)
		comentarios = post.Chispos.all()
		form = CommForm()
		context = {
		'post':post,
		'coments':comentarios,
		'form':form,
		}
		return render(request,template_name,context)

	def post(self, request, slug):
		form = CommForm(request.POST)
		post = Post.objects.get(slug=slug)
		new_com = form.save(commit=False)
		new_com.user = request.user
		new_com.post = post 
		new_com.save()
		return redirect('detalle', slug=slug)  	

class UpdateView(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'nuevo.html'
		form = PostForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		form = PostForm(request.POST,request.FILES)
		new_post = form.save(commit=False)
		new_post.slug = slugify(new_post.titulo)
		new_post.save()
		return redirect('lista')











