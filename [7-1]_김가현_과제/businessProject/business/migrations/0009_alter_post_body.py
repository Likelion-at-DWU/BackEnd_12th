# Generated by Django 4.2.13 on 2024-05-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='', verbose_name='리뷰'),
        ),
    ]
