# Generated by Django 4.0.4 on 2022-06-01 06:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediumish', '0018_alter_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=ckeditor.fields.RichTextField(default=True),
        ),
    ]
