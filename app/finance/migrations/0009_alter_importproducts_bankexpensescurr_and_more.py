# Generated by Django 4.1.3 on 2023-10-01 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_currency_store_importproducts_import_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importproducts',
            name='bankExpensesCurr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bank_expenses_currency', to='finance.currency', verbose_name='Bank Expenses Currency'),
        ),
        migrations.AlterField(
            model_name='importproducts',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='finance.currency', verbose_name='Currency'),
        ),
    ]
