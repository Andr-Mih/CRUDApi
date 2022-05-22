
from .models import News, Comment
from django.forms import ModelForm, widgets
from django import forms

class NewForm(ModelForm):
    class Meta:
        model = News
        fields = ['new_titile', 'new_link', 'new_creation_date', 'new_author_name']
        widgets = {'new_title':forms.HiddenInput()}

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields = ['coment_author', 'coment_title', 'coment_creation_date']
        widgets = {'coment_author_name': forms.HiddenInput()}