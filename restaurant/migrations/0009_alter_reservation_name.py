# Generated by Django 3.2.14 on 2022-08-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20220810_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
