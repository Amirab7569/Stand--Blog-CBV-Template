from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import format_html
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return f'{self.name}'
    
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, related_name="posts")
    body = models.TextField()
    image = models.ImageField(upload_to="images/posts/%Y/%m/%d", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, unique=True)
    status  = models.BooleanField(default=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created",)
        verbose_name = "post"
        verbose_name_plural = "posts"
    
    
    def __str__(self):
        return f'{self.title} - {self.body[:15]}'
    
    def get_absolute_url(self):
        return reverse("home:detail", kwargs={"slug": self.slug})
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
        
    def show_image_admin(self):
        if self.image:
            return format_html(f'<img src= "{self.image.url}" width="80px" hieght="80px">')
        else:
            return format_html("<h3>None Image</h3>")
        
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies",null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body[:35]
    
    
class ContactUs(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
        
    class Meta:
        verbose_name_plural = "Contact Us"
    
    def __str__(self):
        return self.subject
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.post.title}'
    
    class Meta:
        verbose_name = "like"
        verbose_name_plural = "likes"