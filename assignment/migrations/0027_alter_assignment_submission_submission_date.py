# Generated by Django 3.2.7 on 2021-10-20 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0026_auto_20211020_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_submission',
            name='submission_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]