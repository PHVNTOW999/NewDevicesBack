# Generated by Django 4.1.3 on 2023-09-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0003_jobs_data_jobs_date_jobsinfo_workers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobsinfo',
            name='client',
        ),
        migrations.AddField(
            model_name='workers',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='workers',
            name='salary',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='data',
            field=models.ManyToManyField(to='other.jobsinfo', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='workers',
            field=models.ManyToManyField(blank=True, to='other.workers', verbose_name='Workers'),
        ),
    ]
