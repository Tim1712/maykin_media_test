# Generated by Django 3.2.6 on 2021-08-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_rename_hotels_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_city_abb',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
