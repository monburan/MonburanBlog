#coding=utf-8
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,render_to_response
from blog.models import Blog,Aboutme,Friends,Category,Tag
from django.http import Http404
from collections import OrderedDict
import json

def pagination(request,limit,blog_list):
	
	paginator = Paginator(blog_list,limit)
	page = request.GET.get('page')
	
	try:
		return paginator.page(page)
	except PageNotAnInteger:
		return paginator.page(1)
	except EmptyPage:
		return paginator.page(paginator.num_pages)

def get_all_blogs(request):
	limit = 5
	blog_list = Blog.objects.all().order_by('-created')
	blogs = pagination(request,limit,blog_list)
	ctx = {
		'title_type':'index',
		'blogs':blogs,
		'limit':limit,
		}	
	return render_to_response('index.html',ctx)

def get_detail_id(request,blog_id):
	try:
		blog = Blog.objects.get(id=blog_id)
	except Blog.DoesNotExist:
		raise Http404
	ctx = {
		'title_type':'detail',
		'blog':blog,
		}
	return render(request,'details.html',ctx)

def categorys(request):#显示所有分类的名称和文章总数
	id = 0
	datas = OrderedDict()
	categorys = Category.objects.all()
	count = categorys.count()
	ctx = {
		'categorys':categorys,
	}
	return render_to_response('categorys.html',ctx)

def get_category_id(request,c_id):
	
	limit = 5
	blog_list = Blog.objects.filter(category_id=c_id)
	try:	
		blogs = pagination(request,limit,blog_list)
	except blog_list.count() == 0:
		raise Http404
	else:
		ctx = {
			'title_type':'category',
			'title_name':Category.objects.get(id=c_id),
			'blogs':blogs,
			'limit':limit,
		}
		return render_to_response('index.html',ctx)
		
def tags(request):#显示所有标签的名称和文章总数
	
	tags = Tag.objects.all()
	ctx = {
		'tags':tags,
		}
	return render_to_response('tags.html',ctx)
	
def get_tag_id(request,t_id):

	limit = 5
	blog_list = Blog.objects.filter(tag=t_id)

	try:	
		blogs = pagination(request,limit,blog_list)
	except blog_list.count() == 0:
		raise Http404
	else:
		ctx = {
			'title_type':'tag',
			'title_name':Tag.objects.get(id=t_id),
			'blogs':blogs,
			'limit':limit,
		}
		return render_to_response('index.html',ctx)

def about_me(request):
	
	data = Aboutme.objects.get(id=1)

	return render_to_response('aboutme.html',{'aboutme':data})

def friends(request):
	
	data = Friends.objects.get(id=1)
	
	return render_to_response('friends.html',{'friends':data})
# Create your views here.
