# Generated by Django 3.2.14 on 2022-08-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_reservation_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='last_name',
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]