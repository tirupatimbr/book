# Generated by Django 2.1.7 on 2020-02-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0015_auto_20200212_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseimage',
            name='base_image',
            field=models.FileField(blank=True, null=True, upload_to='base_64'),
        ),
    ]