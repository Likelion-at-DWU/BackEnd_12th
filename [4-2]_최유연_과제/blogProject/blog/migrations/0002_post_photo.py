# Generated by Django 5.0.3 on 2024-05-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo', verbose_name='이미지'),
        ),
    ]
