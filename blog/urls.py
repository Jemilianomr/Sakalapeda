from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from accounts import urls as cuentasUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^nuevo/$', views.UpdateView.as_view(), name="nuevo"),
    url(r'^blog/$', views.ListView.as_view(), name="lista"),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
    url(r'^accounts/',include(cuentasUrls))
]
