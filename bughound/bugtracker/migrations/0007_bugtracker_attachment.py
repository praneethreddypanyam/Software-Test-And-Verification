# Generated by Django 4.0.6 on 2022-07-25 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0006_alter_bugtracker_assigned_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugtracker',
            name='attachment',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
