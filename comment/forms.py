from django import forms
from .models import Comment


#리뷰 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']


