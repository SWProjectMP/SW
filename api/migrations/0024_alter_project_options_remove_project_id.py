# Generated by Django 4.1.4 on 2022-12-23 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_project_options_project_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
    ]
