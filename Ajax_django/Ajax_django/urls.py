from django.conf.urls import patterns, include, url
from django.contrib import admin
from ejemplo.views import AutoresView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',AutoresView.as_view()),
    url(r'^ajax_libros/$','ejemplo.views.busqueda_libros'),
)
