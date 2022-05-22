
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'comments'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.NewList.as_view()),
    path('news/<int:pk>', views.NewDetail.as_view()),
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>', views.CommentDetail.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)