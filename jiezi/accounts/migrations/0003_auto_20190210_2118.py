# Generated by Django 2.1.5 on 2019-02-11 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190204_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercharacter',
            options={'ordering': ['time_added', 'character__pk']},
        ),
    ]