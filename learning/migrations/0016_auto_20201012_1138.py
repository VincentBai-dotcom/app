# Generated by Django 3.1.1 on 2020-10-12 11:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20201012_1138'),
        ('learning', '0015_auto_20201012_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningprocess',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='learningprocess',
            name='last_study_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='learningprocess',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='classroom.student'),
        ),
    ]
