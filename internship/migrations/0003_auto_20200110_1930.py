# Generated by Django 3.0 on 2020-01-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0002_auto_20200110_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='think_analytics',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]