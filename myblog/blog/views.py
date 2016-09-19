#coding=utf-8
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,render_to_response
from blog.models import Blog,Aboutme,Friends,Category,Tag
from django.http import Http404
from django.views.defaults import page_not_found,server_error
from collections import OrderedDict


def error404(request):
    #if programe touch Object.DoesNotExist
    #it will return a 404 Httpresponse like -> Http404
    #then error404 will run and return a 404 page 
    return page_not_found(request,template_name='404.html')

def error500(request):
    #same like error404
    return server_error(request,template_name='500.html')

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
    blog_list = Blog.objects.filter(status="p")[::-1]
    blogs = pagination(request,limit,blog_list)
    page = request.GET.get('page')
    ctx = {
        'title_type':'index',
        'blogs':blogs,
        'page':page,
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

    categorys = Category.objects.all()
    ctx = {
        'categorys':categorys,
    }
    return render_to_response('categorys.html',ctx)

def get_category_id(request,c_id):
    
    limit = 3
    blog_list = Blog.objects.filter(category_id=c_id,status="p")
    try:    
        blogs = pagination(request,limit,blog_list)
    except blog_list.count() == 0:
        raise Http404
    else:
        ctx = {
            'title_type':'category',
            'title_name':Category.objects.get(id=c_id),
            'blogs':blogs,
        }
        return render_to_response('index.html',ctx)
        
def tags(request):#显示所有标签的名称和文章总数
    
    tags = Tag.objects.all()
    ctx = {
        'tags':tags,
        }
    return render_to_response('tags.html',ctx)
    
def get_tag_id(request,t_id):

    limit = 3
    blog_list = Blog.objects.filter(tag=t_id,status="p")

    try:    
        blogs = pagination(request,limit,blog_list)
    except blog_list.count() == 0:
        raise Http404
    else:
        ctx = {
            'title_type':'tag',
            'title_name':Tag.objects.get(id=t_id),
            'blogs':blogs,
        }
        return render_to_response('index.html',ctx)

def about_me(request):

    try:    
        data = Aboutme.objects.all()[:1][0]
    except IndexError:
        #if admin didn't write a aboutme page this programe will return a 404 page
        raise Http404
    else:
        return render_to_response('aboutme.html',{'aboutme':data})

def friends(request):

    try: 
        data = Friends.objects.all()[:1][0]
    except IndexError:
        raise Http404
    else:
        return render_to_response('friends.html',{'friends':data})
