# Generated by Django 4.0.4 on 2022-05-22 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('recommendations', models.TextField(default=None)),
                ('ratings_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ratings_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('poster', models.CharField(max_length=200)),
                ('backdrop', models.CharField(max_length=200)),
                ('release_date', models.CharField(max_length=200)),
                ('overview', models.TextField(default=None)),
                ('youtube_id', models.CharField(max_length=200)),
                ('genre', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('movie_id', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated', models.IntegerField(default=0)),
                ('recommendations', models.TextField(default=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
