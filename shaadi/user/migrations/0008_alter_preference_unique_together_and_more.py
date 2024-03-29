# Generated by Django 4.2.7 on 2023-11-10 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_height_height'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='preference',
            name='preferred_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='preference',
            name='preferred_community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.community'),
        ),
        migrations.AddField(
            model_name='preference',
            name='preferred_gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.gender'),
        ),
        migrations.AddField(
            model_name='preference',
            name='preferred_height',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.height'),
        ),
        migrations.AddField(
            model_name='preference',
            name='preferred_maritalstatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.maritalstatus'),
        ),
        migrations.AddField(
            model_name='preference',
            name='preferred_religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.religion'),
        ),
        migrations.RemoveField(
            model_name='preference',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='preferred_user',
        ),
    ]
