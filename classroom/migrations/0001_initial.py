# Generated by Django 3.1.1 on 2020-10-10 12:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0010_auto_20201010_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to='accounts.user')),
                ('study_streak', models.IntegerField(default=0)),
                ('last_study_time', models.DateTimeField(auto_now_add=True)),
                ('last_study_duration', models.DurationField(default=datetime.timedelta(0))),
                ('last_study_vocab_count', models.IntegerField(default=0)),
                ('total_study_duration', models.DurationField(default=datetime.timedelta(0))),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='teacher', serialize=False, to='accounts.user')),
            ],
        ),
    ]
