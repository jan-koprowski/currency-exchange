# Generated by Django 3.2 on 2021-05-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0004_auto_20210504_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantor',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
