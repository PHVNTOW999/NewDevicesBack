# Generated by Django 4.1.3 on 2023-09-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_salarycalc_time_end_work_salarycalc_time_start_work_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importproductsfromarmenia',
            name='wholesalePrice',
        ),
        migrations.AddField(
            model_name='importproductsfromarmenia',
            name='details',
            field=models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details'),
        ),
    ]
