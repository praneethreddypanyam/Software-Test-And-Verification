# Generated by Django 3.2.14 on 2022-07-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0004_rename_program_report_number_bugtracker_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugtracker',
            name='problem',
            field=models.TextField(default='problem'),
        ),
    ]