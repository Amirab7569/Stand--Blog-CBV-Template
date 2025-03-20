from django.contrib import admin
from .models import Post, Category, Comment, ContactUs, Like
# Register your models here.

"""
class CustomFilters(admin.SimpleListFilter):
    title = "بر اساس تکرار"
    parameter_name = "title"
    
    def lookups(self, request, model_admin):
        return (
            ("django", "DJANGO",),
            ("python", "PYTHON",),
        )
        
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains = self.value)
"""



class CammentModelAdmin(admin.TabularInline):
    model = Comment

admin.site.register(Comment)

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","author","status","published","show_image_admin"]
    list_editable = ["status", "published"]
    list_filter = ("published",)
    search_fields = ("title","body")
    inlines = (CammentModelAdmin,)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(ContactUs)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["subject", "email"]
    
    
    
@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['user','post']
    