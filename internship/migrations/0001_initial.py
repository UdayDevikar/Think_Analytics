# Generated by Django 3.0 on 2020-01-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Think_Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('Address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
