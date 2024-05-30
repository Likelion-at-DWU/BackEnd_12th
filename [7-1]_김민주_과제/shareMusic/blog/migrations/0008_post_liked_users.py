# Generated by Django 4.2.11 on 2024-05-30 03:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
