# Generated by Django 4.1.1 on 2022-12-02 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangareader', '0007_task_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['topic', 'difficulty_level', 'name']},
        ),
    ]
