# Generated by Django 5.1.8 on 2025-04-17 07:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('business', 'ビジネス'), ('lifestyle', '生活'), ('other', 'その他')], max_length=20, verbose_name='カテゴリー'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='レビュータイトル')),
                ('text', models.TextField(verbose_name='レビュー内容')),
                ('rate', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='評価')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book', verbose_name='書籍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
