from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.IndexPostListView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("redirect-home/", views.HomePageRedirectView.as_view(), name="redirect-home"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("blog/", views.AllPostView.as_view(), name="blog"),
    path("contact/", views.CreatContactView.as_view(), name="contact"),
    path("messages/", views.ContactMessageShowView.as_view(), name="show-messages"),
    path("messages/edit/<int:pk>", views.UpdateContectView.as_view(), name="edit-message"),
    path("messages/delete/<int:pk>", views.DeleteContactView.as_view(), name="delete-message"),
    
    path("like/<int:pk>/<slug:slug>/", views.like_view, name="post-like"),
    
    path("category/<int:pk>/", views.category_detail, name="category_detail"),
    path("search/", views.search, name="search_post"),
]
