# Generated by Django 2.2.4 on 2019-12-07 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField(max_length=50000)),
                ('thumbnail', models.ImageField(default=True, upload_to='')),
                ('thumbnail_url', models.ImageField(default=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='YtTrending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('thumbnail', models.ImageField(default=True, upload_to='')),
                ('thumbnail_url', models.ImageField(default=True, upload_to='')),
            ],
        ),
    ]
