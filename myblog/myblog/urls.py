import settings

from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf.urls.static import static

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^detail/(\d+)/$','blog.views.get_detail_id',name='blog_get_detail'),
    url(r'^^$','blog.views.get_blogs',name='blog_get_blogs'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^aboutme','blog.views.about_me',name='about_me'),
	url(r'^friends','blog.views.friends',name='friends'),
	url(r'^tags','blog.views.tags',name='tags'),
	url(r'^category','blog.views.categorys',name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += staticfiles_urlpatterns
