# Generated by Django 3.1.2 on 2021-01-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_remove_label_detection_model'),
        ('detection_models', '0002_auto_20201021_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectionmodel',
            name='labels',
            field=models.ManyToManyField(to='labels.Label'),
        ),
    ]
