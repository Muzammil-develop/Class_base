from django.urls import path
from home import views 

urlpatterns = [
    path ('articles' , views.blog_articles.as_view() , name='blog_articles'),
    path ('<int:pk>' , views.blog_articles_detail.as_view() , name='blog_articles_detail'),
]
