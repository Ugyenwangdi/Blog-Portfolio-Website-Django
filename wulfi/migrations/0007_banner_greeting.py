# Generated by Django 4.0 on 2022-07-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wulfi', '0006_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='greeting',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]