# Generated by Django 3.0 on 2020-01-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='think_analytics',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
