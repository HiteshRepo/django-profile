# Generated by Django 3.1.2 on 2020-10-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20201013_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
