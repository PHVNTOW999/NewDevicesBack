# Generated by Django 4.1.3 on 2023-11-10 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_phone_options_alter_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Client', to='info.client', verbose_name='Client'),
        ),
    ]