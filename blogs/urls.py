from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name="index"),
    url('^createblog/$', views.create_blog, name="createblog"),
    url('^viewblog/$', views.view_blog_data, name="viewblog"),
    url('^saveblog/$', views.save_blog_data, name="saveblog"),
    url('^likeblog/$',views.liked_blog, name="likeblog"),
    url('^dislikeblog/$',views.disliked_blog, name="dislikeblog")
]