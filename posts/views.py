from django.shortcuts import render
from django.views.generic import View
from .models import Post



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






