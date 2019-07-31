from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

# Create your views here.
def create(request): #request의 형식에 따라. 'POST'이냐 'GET'이냐
    if request.method == 'POST' :
        forms = NewBlog(request.POST)
        if forms.is_valid():
            post = forms.save(commit = False) #대문자 False 주의!
            post.pub_date = timezone.now()
            post.save()
            return redirect('read')

    elif request.method == 'GET' :
        forms = NewBlog()
        return render(request, 'blog/create.html', {'forms' : forms})

def read(request):
    blogs = Blog.objects.all()   #objects 복수형 주의
    return render(request, 'blog/read.html', {'blogs' : blogs})

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk ) # 수정할 블로그 객체 가져오기
    forms = NewBlog(request.POST, instance = blog) # 가져온 블로그 객체에 맞는 입력공간을 마련하기 : create 이용
    if forms.is_valid():
        forms.save()
        return redirect('read')
    return render(request, 'blog/create.html', {'forms' : forms})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk )  # pk = pk 주의!
    blog.delete()
    return redirect('read')


def detail(request, pk):
    blog_detail = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog_detail})