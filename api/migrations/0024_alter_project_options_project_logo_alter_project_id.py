# Generated by Django 4.1.4 on 2022-12-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_project_options_project_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(),
        ),
    ]