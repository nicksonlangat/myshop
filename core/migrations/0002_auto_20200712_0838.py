# Generated by Django 3.0.8 on 2020-07-12 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='bicycle',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='bicycle',
            name='slug',
        ),
    ]