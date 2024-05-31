# Generated by Django 4.2.13 on 2024-05-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128, verbose_name='프로젝트명')),
                ('language', models.CharField(max_length=128, verbose_name='언어')),
                ('code', models.TextField(default='', verbose_name='코드내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
            ],
        ),
    ]
