# Generated by Django 3.2.5 on 2021-07-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_forum', '0002_forum_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]