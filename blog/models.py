from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
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
    image = models.ImageField(upload_to="images/posts/%Y/%m/%d")
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
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies",null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.body[:35]