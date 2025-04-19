from django.db import models
from django.contrib.auth.models import User
from .consts import MAX_RATE

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Book(models.Model):
    CATEGORY_CHOICES = (
        ("business", "ビジネス"),
        ("lifestyle", "生活"),
        ("other", "その他"),
    )

    title = models.CharField(max_length=100, verbose_name="タイトル")
    thumbnail = models.ImageField(
        upload_to="book/picture", blank=True, null=True, verbose_name="サムネイル"
    )
    text = models.TextField(verbose_name="内容")
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name="カテゴリー"
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="書籍")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー")
    title = models.CharField(max_length=100, verbose_name="レビュータイトル")
    text = models.TextField(verbose_name="レビュー内容")
    rate = models.IntegerField(choices=RATE_CHOICES, verbose_name="評価")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return f"{self.title} - {self.user.username} - {self.book.title}"
