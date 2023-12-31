# Generated by Django 4.1.3 on 2023-10-23 12:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carriers',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('fromCountry', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='From Country')),
                ('toCountry', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='To Country')),
                ('phone', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Carrier',
                'verbose_name_plural': 'Carriers',
            },
        ),
        migrations.CreateModel(
            name='CompletedWorks',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('work', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Work desc')),
                ('amount', models.FloatField(blank=True, default=None, null=True, verbose_name='Amount')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'CompletedWork',
                'verbose_name_plural': 'CompletedWorks',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fromCountry', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='From Country')),
                ('toCountry', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='To Country')),
                ('amount', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Amount')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Import',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('seller', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Seller')),
                ('phone', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Phone')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'Import',
                'verbose_name_plural': 'Imports',
            },
        ),
        migrations.CreateModel(
            name='ImportFromArmenia',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('seller', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Seller')),
                ('phone', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Phone')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('date', models.DateField(blank=True, default=None, null=True, verbose_name='Date')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'ImportFromArmenia',
                'verbose_name_plural': 'ImportFromArmenia',
            },
        ),
        migrations.CreateModel(
            name='ImportProducts',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('quantity', models.FloatField(blank=True, default=None, null=True, verbose_name='Quantity')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Price')),
                ('totalWeight', models.FloatField(blank=True, default=None, null=True, verbose_name='Total Weight')),
                ('weightNeto', models.FloatField(blank=True, default=None, null=True, verbose_name='Neto Weight')),
                ('weightBrutto', models.FloatField(blank=True, default=None, null=True, verbose_name='Brutto Weight')),
                ('percentCustomsCosts', models.FloatField(blank=True, default=None, null=True, verbose_name='Percent Customs Costs')),
                ('percentCustomsPrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Percent Customs Price')),
                ('bankExpensesAmount', models.FloatField(blank=True, default=None, null=True, verbose_name='Bank Expenses Amount')),
                ('bankExpensesPerc', models.FloatField(blank=True, default=None, null=True, verbose_name='Bank Expenses Percent')),
                ('bankExpensesDays', models.IntegerField(blank=True, default=None, null=True, verbose_name='Bank Expenses Days')),
                ('costPrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Cost Price')),
                ('wholesalePerc', models.FloatField(blank=True, default=None, null=True, verbose_name='Wholesale Percent')),
                ('wholesalePrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Wholesale Price')),
                ('retailPerc', models.FloatField(blank=True, default=None, null=True, verbose_name='Retail Percent')),
                ('retailPrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Retail Price')),
                ('incomeFromWholesale', models.FloatField(blank=True, default=None, null=True, verbose_name='Income From Wholesale')),
                ('incomeFromRetail', models.FloatField(blank=True, default=None, null=True, verbose_name='Income From Retail')),
                ('details', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'ImportProduct',
                'verbose_name_plural': 'ImportProducts',
            },
        ),
        migrations.CreateModel(
            name='ImportProductsFromArmenia',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('date', models.DateField(blank=True, default=None, null=True, verbose_name='Date')),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('quantity', models.FloatField(blank=True, default=None, null=True, verbose_name='Quantity')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Price')),
                ('wholesalePrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Wholesale price')),
                ('percentSellingPrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Percent Selling Price')),
                ('totalSellingPrice', models.FloatField(blank=True, default=None, null=True, verbose_name='Selling Price')),
                ('income', models.FloatField(blank=True, default=None, null=True, verbose_name='Income')),
                ('details', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'ImportProductFromArmenia',
                'verbose_name_plural': 'ImportProductsFromArmenia',
            },
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('carrier', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Carrier')),
                ('amount', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Amount')),
                ('repoName', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Repository Name')),
                ('repoDate', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Repository Date')),
                ('repoExpectedTime', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Repository Expected Time')),
                ('repoArrivalTime', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Repository Arrival Time')),
            ],
            options={
                'verbose_name': 'Repo',
                'verbose_name_plural': 'Repos',
            },
        ),
        migrations.CreateModel(
            name='UnitMeas',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Unit measurements',
                'verbose_name_plural': 'Unit measurements',
            },
        ),
        migrations.CreateModel(
            name='Transportations',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('detailsForCarriers', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details For Carriers')),
                ('Carriers', models.ManyToManyField(blank=True, to='finance.carriers', verbose_name='Carriers')),
            ],
            options={
                'verbose_name': 'Transportation',
                'verbose_name_plural': 'transportations',
            },
        ),
        migrations.CreateModel(
            name='SalaryCalc',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('time_start_work', models.TimeField(blank=True, null=True, verbose_name='Time Start Work')),
                ('time_end_work', models.TimeField(blank=True, null=True, verbose_name='Time Start Work')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('CompletedWorks', models.ManyToManyField(blank=True, to='finance.completedworks', verbose_name='Completed Works')),
            ],
            options={
                'verbose_name': 'SalaryCalc',
                'verbose_name_plural': 'SalaryCalc',
            },
        ),
    ]
