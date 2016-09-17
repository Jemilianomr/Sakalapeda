from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from accounts import urls as cuentasUrls
from django.views.static import serve
from django.conf import settings
from posts.api import urls as apiUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^nuevo/$', views.UpdateView.as_view(), name="nuevo"),
    url(r'^sakalapeda.com/$', views.ListView.as_view(), name="lista"),
    url(r'^sakalapeda.com/categoria/(?P<cat>[-\w]+)/$', views.ListView.as_view(), name="categoria"),
    url(r'^sakalapeda.com/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
    url(r'^accounts/',include(cuentasUrls)),
    url(r'^borrar/(?P<pk>\d+)/$', views.PostDelete.as_view(), name="delete"),
    url(
    	regex=r'media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
    url(r'^api/',include(apiUrls)),
]
