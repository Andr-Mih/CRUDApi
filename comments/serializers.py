from rest_framework import serializers
from .models import News, Comment


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'new_titile', 'new_link', 'new_creation_date', 'new_author_name', 'new_votes']


class CommentSerializer(serializers.ModelSerializer):
    #news = serializers.ReadOnlyField(source='news.id')
    class Meta:
        model = Comment
        fields = ['id', 'coment_author', 'coment_title', 'coment_creation_date', 'news']
  