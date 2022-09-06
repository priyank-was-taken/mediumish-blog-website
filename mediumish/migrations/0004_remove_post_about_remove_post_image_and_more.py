# Generated by Django 4.0.4 on 2022-05-31 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediumish', '0003_delete_story'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='about',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Post', to='mediumish.blog'),
        ),
    ]