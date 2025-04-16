from django.db import models


class Book(models.Model):
    CATEGORY_CHOICES = (
        ("busiiness", "ビジネス"),
        ("lifestyle", "生活"),
        ("other", "その他"),
    )

    title = models.CharField(max_length=100, verbose_name="タイトル")
    text = models.TextField(verbose_name="内容")
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, verbose_name="カテゴリー"
    )

    def __str__(self):
        return self.title
