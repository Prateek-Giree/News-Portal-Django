# Generated by Django 5.0.7 on 2024-07-22 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_news', '0002_alter_news_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='news',
            name='summary',
        ),
    ]
