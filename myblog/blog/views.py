from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,render_to_response
from blog.models import Blog,Comment,Aboutme,Friends,Category,Tag
from django.http import Http404
from blog.commentform import CommentForm

def get_blogs(request):
    limit = 3
    blog_list = Blog.objects.all().order_by('-created')
    paginator = Paginator(blog_list,limit)
    page = request.GET.get('page')
	
    try:
    	blogs = paginator.page(page)
    except PageNotAnInteger:
    	blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    ctx = {
        'blogs':blogs
    }	
    return render_to_response('index.html',ctx)

def get_detail_id(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form
           }
    return render(request,'details.html',ctx)

def about_me(request):
	
	data = Aboutme.objects.get(id=1)

	return render_to_response('aboutme.html',{'aboutme':data})
def friends(request):
	
	data = Friends.objects.get(id=1)
	
	return render_to_response('friends.html',{'friends':data})

def tags(request):
	
	data = Tag.objects.all()
	return render_to_response('tags.html',{'tags':data})

def categorys(request):
	
	data = Category.objects.all()
	return render_to_response('categorys.html',{'categorys':data})

# Create your views here.
