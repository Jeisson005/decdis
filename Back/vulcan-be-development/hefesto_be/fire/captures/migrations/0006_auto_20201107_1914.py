# Generated by Django 3.1.2 on 2020-11-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0005_auto_20201107_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capture',
            name='calibr_image_name',
            field=models.CharField(default='1604776470.PNG', help_text='Camera calibration image name', max_length=255, null=True, verbose_name='camera calibration image name'),
        ),
    ]
