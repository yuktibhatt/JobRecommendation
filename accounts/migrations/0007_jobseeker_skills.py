# Generated by Django 3.1.2 on 2020-10-06 06:54

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200930_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='skills',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]
