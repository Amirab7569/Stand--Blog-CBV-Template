from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Comment
from django.core.paginator import Paginator
# Create your views here.

def index_view(request):
    posts = Post.objects.all()
    recent_post = Post.objects.all()[:3]
    return render(request, "home/index.html", {"posts":posts})


def blog_view(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get("page")
    obj_list = paginator.get_page(page_number)
    return render(request, "home/blog.html",{"posts":obj_list})


def about_view(request):
    return render(request, "home/about.html")


def contact_view(request):
    return render(request, "home/contact.html")


def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        Comment.objects.create(body=body, post=post, user=request.user, parent=parent_id)
        
    return render(request, "home/post-details.html",{"post":post})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    # Found post with this category
    posts = category.posts.all()
    return render(request, "home/blog.html",{"posts":posts})


def search(request):
    q = request.GET.get("q")
    # filter title with "q" parameter
    posts = Post.objects.filter(title__icontains=q)
    paginator = Paginator(posts, 1)
    page_number = request.GET.get("page")
    obj_list = paginator.get_page(page_number)
    return render(request, "home/blog.html", {"posts":obj_list})