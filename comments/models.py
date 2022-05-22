from django.db import models
from django.db.models.deletion import CASCADE

class News(models.Model):
    new_titile = models.CharField(max_length=100, null = False)
    new_link = models.URLField()
    new_creation_date = models.DateField(null=False)
    new_author_name = models.CharField(max_length=30, null=False)
    new_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.new_titile

class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    coment_author = models.CharField(max_length=40, null=False)
    coment_title = models.TextField(max_length=300, null=False)
    coment_creation_date = models.DateField(null = False)

    def __str__(self):
        return self.coment_title




# Create your models here.
