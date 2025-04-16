from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text", "category"]
        labels = {
            "title": "タイトル",
            "text": "内容",
            "category": "カテゴリー",
        }
