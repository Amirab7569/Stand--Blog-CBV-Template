from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Category, Comment, ContactUs, Like
from django.core.paginator import Paginator
from .forms import ContactForm
from django.http import JsonResponse
#  class-base
from django.views import View
from django.views.generic import (
    ListView,
    TemplateView,
    RedirectView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# custom mixins
from .mixins import CustomLoginRequiredMixins


# Create your views here.

"""
Index View FBV

def index_view(request):
    posts = Post.objects.all()
    return render(request, "home/index.html", {"posts":posts})
"""

"""
def blog_view(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get("page")
    obj_list = paginator.get_page(page_number)
    return render(request, "home/blog.html",{"posts":obj_list})
"""

"""
def about_view(request):
    return render(request, "home/about.html")
"""

"""
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your text already send it", "success")
            return redirect("home:contact")
    else:
        form = ContactForm() 
    return render(request, "home/contact.html", {"form":form})
"""

"""
def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        Comment.objects.create(body=body, post=post, user=request.user, parent=parent_id)
        
    return render(request, "home/post-details.html",{"post":post})
"""

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



class IndexPostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "home/index.html"
    

class AboutView(TemplateView):
    template_name = "home/about.html"
    

class HomePageRedirectView(RedirectView):
    # url = "/blog/"
    pattern_name = "home:blog"
    query_string = False
    

class PostDetailView(DetailView):
    model = Post
    template_name = "home/post-detail.html"   
    """ Another attribute """ 
    # context_object_name =  "post"
    # slug_url_kwarg = ""
    # pk_url_kwarg = ""
    # queryset = ""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.like.filter(post__slug=self.object.slug, user_id = self.request.user.id).exists():
            context["is_like"] = True
        else:
            context["is_like"] = False
        return context
    
    
class AllPostView(CustomLoginRequiredMixins ,ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    context_object_name = "posts"
    template_name = "home/blog.html"
    paginate_by = 1
    
    
class ContactUsView(FormView):
    template_name = "home/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("home:index")
    
    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)     
        return super().form_valid(form)
    

class CreatContactView(CreateView):
    model = ContactUs
    fields = ("subject", "text",)
    success_url =  reverse_lazy("home:index")
    template_name = "home/contact.html"
    
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = ContactUs.objects.all()
        return context
    """
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
    
    
class ContactMessageShowView(ListView):
    model = ContactUs
    template_name = "home/contact_list.html"
    context_object_name = "messages"


class UpdateContectView(UpdateView):
    model = ContactUs
    fields = ("subject","text",)
    template_name = "home/contact_update.html"
    success_url = reverse_lazy("home:show-messages")
    

class DeleteContactView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy("home:show-messages")
    template_name = "home/confirm_delete_contact.html"
    
    
def like_view(request, slug, pk):
    try:
        like = Like.objects.get(post__slug=slug, user_id = request.user.id)
        like.delete()
        return JsonResponse({"response":"unlike post"})
    except:
        Like.objects.create(post_id=pk,user_id = request.user.id)
        return JsonResponse({"response":"like post"})
    
