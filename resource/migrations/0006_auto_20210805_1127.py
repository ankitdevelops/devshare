# Generated by Django 3.2.5 on 2021-08-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0005_auto_20210805_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': 'Resource', 'verbose_name_plural': 'Resource'},
        ),
        migrations.AddField(
            model_name='resource',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='on_homepage',
            field=models.BooleanField(default=False),
        ),
    ]
