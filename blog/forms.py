from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'text', 'photo', 'price_2hour', 'price_hour', 'price_night')
