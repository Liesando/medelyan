# Generated by Django 2.0 on 2017-12-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171220_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='multiple_choice',
            field=models.BooleanField(default=False),
        ),
    ]
