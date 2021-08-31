# Generated by Django 3.2.6 on 2021-08-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100)),
                ('abb', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100)),
                ('abb', models.CharField(blank=True, max_length=100)),
                ('hotel', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]