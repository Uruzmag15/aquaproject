from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^catalog/', views.catalog, name='catalog'),
	url(r'^aboutus/', views.aboutus, name='aboutus'),
	url(r'^partnership/', views.partnership, name='partnership'),
	url(r'^contacts/', views.contacts, name='contacts'),
	url(r'^brand/(?P<pk>[0-9]+)/$', views.brand_detail, name='brand_detail'),
	url(r'^favicon\.ico$', RedirectView.as_view(url='/static/siteapp/img/favicon.ico', permanent=True)),
]
