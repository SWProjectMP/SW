# Generated by Django 4.1.4 on 2022-12-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_projectimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('pk',)},
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.IntegerField(default=None, unique=True),
            preserve_default=False,
        ),
    ]
