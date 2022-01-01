from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

import blog
from blog.forms import PostForm
from blog.models import Post

def index(request):
    #블로그 메인 페이지
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    #글 쓰기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)

@login_required(login_url='common:login')
def blog_delete(request, blog_id):
    #블로그 삭제
    blog = get_object_or_404(Post, pk=blog_id)
    blog.delete()
    return redirect('blog:index')