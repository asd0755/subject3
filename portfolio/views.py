from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Portfolio
from .forms import NewPortfolio
from django.http import HttpResponse

# Create your views here.
def createp(request): #request의 형식에 따라. 'POST'이냐 'GET'이냐
    if request.method == 'POST' :
        forms = NewPortfolio(request.POST, request.FILES)
        if forms.is_valid():
            post = forms.save(commit = False) #대문자 False 주의!
            post.pub_date = timezone.now()
            post.save()
            return redirect('readp')

    elif request.method == 'GET' :
        form = NewPortfolio()
        return render(request, 'portfolio/createp.html', {'form' : form})

def read(request):
    portfolios = Portfolio.objects.all()  #objects 복수형 주의
    return render(request, 'portfolio/read.html', {'portfolios' : portfolios})

def update(request, pk):
    portfolio = get_object_or_404( Portfolio, pk = pk ) # 수정할 블로그 객체 가져오기
    form = NewPortfolio(request.POST, request.FILES, instance = portfolio) # 가져온 블로그 객체에 맞는 입력공간을 마련하기 : create 이용
    if form.is_valid():
        form.save()
        return redirect('readp')
    return render(request, 'portfolio/createp.html', {'form' : form})

def delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk = pk )  # pk = pk 주의!
    portfolio.delete()
    return redirect('readp')

def detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'portfolio/detail.html', {'portfolio': portfolio})

