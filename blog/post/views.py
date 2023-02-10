from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect, Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.



def post_delete(request,id):
    post=Post.objects.get(id=id)
    post.delete()

    return redirect("index")
def post_index(request):
    posts=Post.objects.all()
    return render(request,'post/index.html',{"posts":posts})
def post_datail(request,id):
    post=Post.objects.get(id=id)
    context={
        "post":post
    }
    return render(request,'post/datail.html',context)
def post_create(request):
    form=PostForm()
    """
    if request.method=="POST":
        #1. yontem kayıt etmek için 
        # title=request.POST["title"]
        # content=request.POST["content"]
        # Post.objects.create(content=content,title=title)
    """
    
    
    #form=PostForm(request.POST or None)#kayıt ekleme 2.yöntem
    if form.is_valid():
        form.save()
        messages.success(request,"basarılı bir şekilde olusturdunuz")

        
    context={
        "form":form,
    }
    return render(request,'post/form.html',context)

def post_update(request,id):#BURASI TAM CALIŞMIYOR TEKRAR POST OLUSUYOR GUNCELLENMEESİ GEREKİYOR 
    #post=Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    #form=PostForm(request.POST or None,instance=post)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
  #  print(form)
    if form.is_valid():
        form.save()
        messages.success(request,"postu tekrar olusturdunuz ama")
        return HttpResponseRedirect(post.get_absolute_url())

    # post.title=request.POST["title"]
    # post.content=request.POST["content"]
    # post.save()   

    context={
        "form":form,
    }
    return render(request, "post/form.html", context)

"""def post_update(request, id):

   

    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)"""