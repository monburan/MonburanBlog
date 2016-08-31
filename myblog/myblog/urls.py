#coding=utf-8
import settings

from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf.urls.static import static

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^detail/(\d+)/$','blog.views.get_detail_id',name='blog_get_detail'),#具体文章详情页
    url(r'^^$','blog.views.get_all_blogs',name='blog_get_blogs'),#主页，显示文章
    url(r'^admin/', include(admin.site.urls)),
	url(r'^aboutme','blog.views.about_me',name='about_me'),#关于
	url(r'^friends','blog.views.friends',name='friends'),#好友
	url(r'^tags','blog.views.tags',name='tags'),#显示所有tag
	url(r'^categorys','blog.views.categorys',name='all_categorys'),#显示所有category
	url(r'^category/(\d+)/$','blog.views.get_category_id',name='blog_get_category'),#根据id显示category
	url(r'^tag/(\d+)/$','blog.views.get_tag_id',name='blog_get_tag'),#根据id显示tag
#	url(r'^error','blog.views.error')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += staticfiles_urlpatterns
