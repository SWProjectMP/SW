# Generated by Django 4.1.4 on 2022-12-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_project_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
