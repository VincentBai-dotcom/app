# Generated by Django 2.1.7 on 2020-08-28 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_is_guest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercharacter',
            options={'ordering': ['mastered', 'definition_1_mastered', 'pinyin_mastered']},
        ),
        migrations.RemoveField(
            model_name='usercharacter',
            name='EF',
        ),
        migrations.RemoveField(
            model_name='usercharacter',
            name='interval',
        ),
        migrations.RemoveField(
            model_name='usercharacter',
            name='time_last_learned',
        ),
        migrations.RemoveField(
            model_name='usercharacter',
            name='times_learned',
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='definition_1_in_a_row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='definition_1_in_a_row_required',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='definition_1_mastered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='definition_1_time_last_studied',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='learned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='mastered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='pinyin_in_a_row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='pinyin_in_a_row_required',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='pinyin_mastered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='pinyin_time_last_studied',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
