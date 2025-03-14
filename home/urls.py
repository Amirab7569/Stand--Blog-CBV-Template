from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("about/", views.about_view, name="about"),
    path("blog/", views.blog_view, name="blog"),
    path("contact/", views.contact_view, name="contact"),
    path("post/<slug:slug>/", views.detail_view, name="detail"),
    path("category/<int:pk>/", views.category_detail, name="category_detail"),
    path("search/", views.search, name="search_post"),
]
