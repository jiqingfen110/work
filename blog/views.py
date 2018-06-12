from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType

#blogs列表页面views
def blog_list(request):
    context = dict()
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog/blog_list.html',context)
#blog内容页views
def bolg_detail(request,blog_pk):
    context = dict()
    context['blog'] = get_object_or_404(Blog,id = blog_pk)
    return render_to_response('blog/blog_detail.html',context)

#blogs分类views
def blogs_with_type(request,blog_type_pk):
    context = dict()
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html',context)
