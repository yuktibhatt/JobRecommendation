# Generated by Django 3.1 on 2020-10-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201007_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
