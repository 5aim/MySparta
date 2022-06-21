from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

from blog.models import Article as ArticleModel

# 10. CBV : 로그인 한 사용자의 게시글의 제목을 리턴
class ArticleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        
        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles] # list 제목 축약 문법

        titles = []

        for article in articles:
            titles.append(article.title)

        return Response({"article_list": titles})