# Generated by Django 3.1.5 on 2021-04-13 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0002_auto_20210413_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='screening_mpei',
            new_name='screening',
        ),
    ]