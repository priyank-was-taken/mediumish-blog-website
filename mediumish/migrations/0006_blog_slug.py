# Generated by Django 4.0.4 on 2022-05-31 10:57

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mediumish', '0005_remove_authorprofile_user_remove_post_blog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=['title']),
        ),
    ]
