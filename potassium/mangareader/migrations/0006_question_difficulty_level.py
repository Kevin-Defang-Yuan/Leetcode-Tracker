# Generated by Django 4.1.1 on 2022-11-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangareader', '0005_collection_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]