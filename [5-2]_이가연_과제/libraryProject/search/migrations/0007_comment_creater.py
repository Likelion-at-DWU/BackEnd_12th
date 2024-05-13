# Generated by Django 4.2.11 on 2024-05-13 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0006_rename_u_author_book_creater'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='creater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
