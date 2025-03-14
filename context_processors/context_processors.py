from blog.models import Post, Category


def recent_post(request):
    recent_post = Post.objects.all().order_by("-created")
    return {"recent_post":recent_post}

def categories(request):
    categories = Category.objects.all()
    return {"categories":categories}