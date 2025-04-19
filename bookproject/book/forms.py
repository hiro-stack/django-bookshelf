from django.forms import ModelForm
from .models import Book
from .models import Review


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text", "category", "thumbnail", "user"]
        labels = {
            "title": "タイトル",
            "text": "内容",
            "category": "カテゴリー",
            "thumbnail": "サムネイル",
            "user": "ユーザー",
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["title", "text", "rate"]
        labels = {
            "title": "レビュータイトル",
            "text": "本文",
            "rate": "星の数",
        }
