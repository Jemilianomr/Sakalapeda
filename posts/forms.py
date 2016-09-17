from django import forms
from .models import Post, Comentario, Asistencia


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo','organizador','fecha','lugar','cuerpo','imagen','categoria']

class CommForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['cuerpo']		

class AstForm(forms.ModelForm):
	class Meta:
		model = Asistencia
		fields = ['user']	