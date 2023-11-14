# Generated by Django 4.1.3 on 2023-11-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_remove_meet_communicationmethod_meet_emails_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='email',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='phone',
            new_name='num',
        ),
        migrations.AlterField(
            model_name='meet',
            name='phones',
            field=models.ManyToManyField(blank=True, to='info.phone', verbose_name='phones'),
        ),
    ]
