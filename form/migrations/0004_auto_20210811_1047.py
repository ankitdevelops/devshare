# Generated by Django 3.2.6 on 2021-08-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='resolved_on_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
