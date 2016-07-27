from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from advs import views as advs_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', advs_views.List.as_view(), name='advs-list'),
    url(r'^(?P<pk>\d+)$', advs_views.Detail.as_view(), name='advs-detail'),
]

urlpatterns += staticfiles_urlpatterns()
