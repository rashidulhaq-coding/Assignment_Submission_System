# Generated by Django 3.2.7 on 2021-10-03 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_auto_20211001_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subjects', models.ManyToManyField(blank=True, null=True, to='assignment.Subject')),
            ],
            options={
                'verbose_name': 'Semester',
                'verbose_name_plural': 'Semesters',
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.semester')),
            ],
            options={
                'verbose_name': 'batch',
                'verbose_name_plural': 'batches',
            },
        ),
        migrations.AddField(
            model_name='student_user',
            name='batch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assignment.batch'),
            preserve_default=False,
        ),
    ]