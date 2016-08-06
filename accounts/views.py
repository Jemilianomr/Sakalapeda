from django.shortcuts import render
from django.views.generic import View


class Perfil(View):
	def get(self,request):
		template_name = 'accounts/perfil.html'
		context = {}
		return render(request, template_name, context)
