# Generated by Django 4.2.7 on 2023-11-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_preferred_age_preference_max_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='preferred_height',
        ),
        migrations.AddField(
            model_name='preference',
            name='max_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='min_height',
            field=models.IntegerField(null=True),
        ),
    ]
