# Generated by Django 4.1.4 on 2022-12-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_profile_profile_id_alter_tags_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='display_tag',
            field=models.CharField(default='', max_length=20),
        ),
    ]
