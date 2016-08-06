from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^profile/$', views.Perfil.as_view(),name="perfil"),
]