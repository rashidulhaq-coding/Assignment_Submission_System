# Generated by Django 3.2.7 on 2021-10-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0016_auto_20211009_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
