# Generated by Django 4.2.13 on 2024-05-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='review_photo', verbose_name='이미지'),
        ),
    ]
