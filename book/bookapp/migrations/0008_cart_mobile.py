# Generated by Django 2.2.7 on 2019-12-13 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0007_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='mobile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.Mobile'),
        ),
    ]
