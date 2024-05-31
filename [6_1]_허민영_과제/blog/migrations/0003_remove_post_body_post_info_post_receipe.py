# Generated by Django 5.0.6 on 2024-05-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='info',
            field=models.TextField(default='', verbose_name='정보'),
        ),
        migrations.AddField(
            model_name='post',
            name='receipe',
            field=models.TextField(default='', verbose_name='레시피'),
        ),
    ]
