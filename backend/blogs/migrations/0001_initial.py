# Generated by Django 2.0.1 on 2018-01-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
