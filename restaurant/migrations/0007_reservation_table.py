# Generated by Django 3.2.14 on 2022-08-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_rename_total_people_reservation_number_of_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Table 1'), (2, 'Table 2'), (3, 'Table 3'), (4, 'Table 4'), (5, 'Table 5'), (6, 'Table 6'), (7, 'Table 7'), (8, 'Table 8')], null=True),
        ),
    ]