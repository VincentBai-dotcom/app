# Generated by Django 3.1.1 on 2020-10-12 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='last_study_duration',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_study_time',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_study_vocab_count',
        ),
        migrations.RemoveField(
            model_name='student',
            name='study_streak',
        ),
    ]
