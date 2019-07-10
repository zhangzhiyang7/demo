from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    context = {'blog': blog}
    return render_to_response('blog/blog_detail.html', context)


def blog_with_type(request, blog_type_pk):
    # 获取到匹配blog_type_pk的BlogType对象，此时例如blog_type = 1
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    # 筛选blog_type为1的blogs,传入Blog对象与blog_type的值
    context = {'blogs': Blog.objects.filter(blog_type=blog_type),
               'blogs_type': blog_type}
    return render_to_response('blog/blog_with_type.html', context)

