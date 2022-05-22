from django.core.paginator import Paginator
from django.db.models import fields
from django.shortcuts import render

import re
from datetime import date, datetime
from rest_framework import generics

from .models import News, Comment
from .serializers import NewSerializer, CommentSerializer


def index(request):
    null_vote()
    record_list = News.objects.all()

    #paginator = Paginator(record_list, 5)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    return render(request, 'comments/index.html', {'record_list': record_list})


def null_vote():
    object = News.objects.all()
    hours= datetime.now().hour
    minut = datetime.now().minute
    if hours == 23 and minut > 59:
        for obj in object:
            obj.new_votes = 0
            obj.save()

class NewList(generics.ListCreateAPIView):
    queryset=News.objects.all()
    serializer_class = NewSerializer

class NewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=News.objects.all()
    serializer_class = NewSerializer

class CommentList(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer

    #def perform_create(self, serializer):
        #serializer.save(new=self.request.news)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer


    
