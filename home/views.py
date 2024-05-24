from django.shortcuts import render
from home.models import Blog
from home.api_file.serializer import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class blog_articles (APIView):

    def get (self ,request):
        articles = Blog.objects.all () 
        serializer = BlogSerializer (articles , many= True)
        return Response (serializer.data)
    
    def post (self , request ):
        serializer = BlogSerializer (data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
class blog_articles_detail (APIView):

    def get (self , request , pk):
        try :
            article = Blog.objects.get (pk = pk)
        except :
            return Response ({"Error" : 'Article is not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer (article)
        return Response (serializer.data)
    
    def put (self , request , pk):
        article = Blog.objects.get (pk = pk)
        serializer = BlogSerializer (article , data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
    def  delete (self , request , pk):
        article = Blog.objects.get (pk = pk)
        article.delete ()
        return Response (status=status.HTTP_204_NO_CONTENT)
