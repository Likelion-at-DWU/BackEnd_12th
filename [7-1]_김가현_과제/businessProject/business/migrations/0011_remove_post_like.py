# Generated by Django 4.2.13 on 2024-05-26 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_alter_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
