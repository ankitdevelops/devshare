# Generated by Django 3.2.5 on 2021-08-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='resource_info',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
