# Generated by Django 3.1.5 on 2021-04-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_information', '0002_booking_screening'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['id']},
        ),
    ]
