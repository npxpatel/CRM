# Generated by Django 5.1.3 on 2024-11-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_rename_origanisation_agent_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(default=True),
        ),
    ]
