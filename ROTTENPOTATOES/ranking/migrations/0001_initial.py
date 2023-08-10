# Generated by Django 4.2.1 on 2023-08-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('release_year', models.IntegerField(max_length=4)),
                ('image', models.CharField(max_length=4)),
                ('rate', models.FloatField(max_length=4)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]