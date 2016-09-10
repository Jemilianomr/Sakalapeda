from django.contrib import admin
from .models import Post, Comentario, Categoria


class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo','slug','fecha','publicado')
	list_filter = ('publicado','fecha')
	search_fields = ('titulo','cuerpo')
	prepopulated_fields = {'slug':('titulo',)}

admin.site.register(Post, PostAdmin)

admin.site.register(Comentario)
admin.site.register(Categoria)

