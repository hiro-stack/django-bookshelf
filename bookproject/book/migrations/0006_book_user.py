# Generated by Django 5.1.6 on 2025-04-19 05:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_thumbnail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
            preserve_default=False,
        ),
    ]
