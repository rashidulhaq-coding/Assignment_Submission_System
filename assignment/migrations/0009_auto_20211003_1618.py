# Generated by Django 3.2.7 on 2021-10-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_auto_20211003_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='courses',
        ),
        migrations.AddField(
            model_name='semester',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='assignment.Course'),
        ),
    ]
