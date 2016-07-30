from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
	titulo = models.CharField(max_length=140)
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField()
	publicado = models.BooleanField(default=False)
	slug = models.SlugField(max_length=500,blank=True,null=True) #esto es un slug

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('detalle',args=[self.slug])
