# Generated by Django 3.1.3 on 2020-12-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='published_at',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
