# Generated by Django 3.2.7 on 2021-09-20 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20210920_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='hod',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to='assignment.hod_user'),
        ),
    ]
