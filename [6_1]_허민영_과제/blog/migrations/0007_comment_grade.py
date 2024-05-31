# Generated by Django 5.0.6 on 2024-05-30 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='grade',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
