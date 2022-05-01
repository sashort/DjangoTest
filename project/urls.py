from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from books.views import book_list, book_detail, hellr, FormBasics

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', index),
    #url(r'^health$', health),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hellr$', hellr),
    url(r'^$', book_list),
    url(r'^books/<int:id>$', book_detail),
	url(r'^forms-basics', FormsBasics.as_view())
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
