# Generated by Django 4.1.3 on 2023-11-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_alter_meet_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='isActive',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Active'),
        ),
    ]
