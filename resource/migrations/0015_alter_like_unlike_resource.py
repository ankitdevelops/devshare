# Generated by Django 3.2.6 on 2021-08-09 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0014_like_unlike_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_unlike',
            name='resource',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='resource.resource'),
        ),
    ]
