from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect, Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.utils.text import slugify
# Create your views here.



def post_delete(request,slug):
    if not request.user.is_authenticated():
       return  Http404()
    post=Post.objects.get(slug=slug)
    post.delete()

    return redirect("index")
def post_index(request):
    post_list = Post.objects.all()
    quary=request.GET.get("q")
    if quary:
        post_list=post_list.filter(
            Q(title__icontains=quary)|
            Q(content__icontains=quary)|
            Q(user__first_name__icontains=quary)|
            Q(user__last_name__icontains=quary)
        ).distinct()
    paginator = Paginator(post_list, 2) # Show 25 contacts per page. burada sayfalamayı gösteriyoruz 
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
        
    except PageNotAnInteger:
        #if page is not an ınteger,deliver first page.
        posts=paginator.page(1)
    except EmptyPage:
        #if page is out  of renge (e.g. 9999),deliver last of results.
        posts=paginator.page(paginator.num_pages)
    
    return render(request,'post/index.html',{"posts":posts})
def post_datail(request,slug):
    post=Post.objects.get(slug=slug)
    
    form=CommentForm(request.POST or None)#kayıt ekleme 2.yöntem
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    
    context={
        "post":post,
        "form":form
    }

    return render(request,'post/datail.html',context)
def post_create(request):
    if not request.user.is_authenticated:
         return Http404()
    form=PostForm()
    """
    if request.method=="POST":
        #1. yontem kayıt etmek için 
        # title=request.POST["title"]
        # content=request.POST["content"]
        # Post.objects.create(content=content,title=title)
    """
    
    
    form=PostForm(request.POST or None,request.FILES or None)#kayıt ekleme 2.yöntem
    if form.is_valid():
        post=form.save(commit=False)
        post.user=request.user
        post.save()
     
        messages.success(request,"basarılı bir şekilde olusturdunuz")
        return HttpResponseRedirect(post.get_absolute_url())
        
    context={
        "form":form,
    }
    return render(request,'post/form.html',context)
def post_update(request,slug): 
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,"postu tekrar olusturdunuz ama")
        return HttpResponseRedirect(post.get_absolute_url())

    context={
        "form":form,
    }
    return render(request, "post/form.html", context)

