# Generated by Django 5.0.4 on 2024-05-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summerfood',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='summer_photo', verbose_name='이미지'),
        ),
    ]
