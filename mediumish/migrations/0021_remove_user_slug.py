# Generated by Django 4.0.4 on 2022-06-01 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediumish', '0020_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]