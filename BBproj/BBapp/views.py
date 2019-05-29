from django.shortcuts import render, redirect
from .models import Blog #Blog모델을 가져와서 쓸꺼니깐 위에 적어줌
from django.core.paginator import Paginator

def index(request):
    posts = Blog.objects.all() #Blog모델에서 만든거 다 가져와서 posts에 때려박아넣음
    paginator = Paginator(posts,5)
    now_page = request.GET.get('page')
    posts = paginator.get_page(now_page)
    context={ # context라고 가공?
        "posts":posts
    }
    return render(request, 'index.html',context) # index.html에 context도 같이 보냄

def detail(request, post_id): # url로부터 post_id를 받아옴
    post = Blog.objects.get(id= post_id) # Blog모델에서 만든거를 가져오는데 id가 post_id와 같은것만 가져옴
    context ={
        "post":post
    }
    return render(request, 'detail.html', context)

def write(request): #GET 은 검색을 위함, POST는 데이터를 전송하고 전송된 데이터에 대한 결과값을 돌려받기 위함
    if request.method == "GET":
        return render(request, 'write.html')
    
    elif request.method == "POST":
        post=Blog()
        post.user = request.user
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.category=request.POST['category']
        post.save()

        return redirect(index)


def update(request, post_id):
    if request.method == "GET":
        post = Blog.objects.get(id= post_id) # Blog모델에서 만든거를 가져오는데 id가 post_id와 같은것만 가져옴
        context ={
            "post":post
        }
        return render(request, "update.html",context)

    elif request.method == "POST":
        post = Blog.objects.get(id= post_id)
        post.title =request.POST['title']
        post.content =request.POST['content']
        post.save()

        return redirect(index)

def delete(request, post_id):
    post = Blog.objects.get(id=post_id)
    post.delete()

    return redirect(index)

def search(request):
    search_title = request.GET['search']
    search_category = request.GET['category2'] #index에서 쓰는 카테고리임
    if search_category=="제목":
        posts=Blog.objects.filter(title__icontains=search_title) #필터는 조건에 부합하는 것을 다 가져옴. get은 하나만 가져옴
    elif search_category=="내용":
        posts=Blog.objects.filter(content__icontains=search_title)
    elif search_category=="제목+내용":
        posts=(Blog.objects.filter(content__icontains=search_title) | Blog.objects.filter(title__icontains=search_title))
    context={
        "posts" : posts
    }
    return render(request, 'search.html', context)

def category(request):
    search_category = request.GET['category']
    posts=Blog.objects.filter(category__icontains=search_category)
    context={
        "posts" : posts
    }
    return render(request, 'category.html', context)