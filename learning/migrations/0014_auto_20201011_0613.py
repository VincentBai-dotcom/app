# Generated by Django 3.1.1 on 2020-10-11 06:13

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0013_auto_20201011_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningprocess',
            name='state',
            field=django_fsm.FSMIntegerField(choices=[(10, 'decide'), (20, 'start_learn'), (30, 'done_learn'), (40, 'start_relearn'), (50, 'done_relearn'), (60, 'tolerant_review'), (70, 'test_review'), (80, 'finish')], default=10),
        ),
    ]
