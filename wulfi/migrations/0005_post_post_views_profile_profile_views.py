# Generated by Django 4.0 on 2022-03-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulfi', '0004_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]