from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, hellr, book_list, book_detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hellr$', hellr),
    path('', book_list),
	path('<id>/', book_detail),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
