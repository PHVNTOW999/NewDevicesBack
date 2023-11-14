# Generated by Django 4.1.3 on 2023-10-31 15:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_email_phone_messenger_alter_meet_datetime_and_more'),
        ('finance', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Craft',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
                ('date_start', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date Start')),
                ('date_challenge', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date Challenge')),
                ('date_end', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date End')),
                ('sell_retail_price', models.FloatField(blank=True, default=None, null=True, verbose_name='Sell Retail Price')),
                ('sell_retail_perc', models.FloatField(blank=True, default=None, null=True, verbose_name='Sell Retail Percent')),
                ('sell_wholesale_price', models.FloatField(blank=True, default=None, null=True, verbose_name='Sell Wholesale Price')),
                ('sell_wholesale_perc', models.FloatField(blank=True, default=None, null=True, verbose_name='Sell Wholesale Percent')),
                ('rent_retail_price', models.FloatField(blank=True, default=None, null=True, verbose_name='Rent Retail Price')),
                ('rent_retail_perc', models.FloatField(blank=True, default=None, null=True, verbose_name='Rent Retail Percent')),
                ('rent_wholesale_price', models.FloatField(blank=True, default=None, null=True, verbose_name='Rent Wholesale Price')),
                ('rent_wholesale_perc', models.FloatField(blank=True, default=None, null=True, verbose_name='Rent Wholesale Percent')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Craft',
                'verbose_name_plural': 'Crafts',
            },
        ),
        migrations.CreateModel(
            name='CraftUnit',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('date_start', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date Start')),
                ('quantity', models.FloatField(blank=True, default=None, null=True, verbose_name='Quantity')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Price')),
                ('date_expected', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date Challenge')),
                ('date_end', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date End')),
                ('details', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'CraftUnit',
                'verbose_name_plural': 'CraftUnits',
            },
        ),
        migrations.CreateModel(
            name='CraftUnitExpenses',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('quantity', models.FloatField(blank=True, default=None, null=True, verbose_name='Quantity')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Price')),
                ('date', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Order Date')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Craft Unit Expenses',
                'verbose_name_plural': 'Craft Units Expenses',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('no', models.IntegerField(blank=True, default=None, null=True, verbose_name='No')),
                ('name', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryCalcWorker',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.workers', verbose_name='Worker')),
            ],
            options={
                'verbose_name': 'SalaryCalc',
                'verbose_name_plural': 'SalaryCalc',
            },
        ),
        migrations.CreateModel(
            name='TransportationUnit',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Active')),
                ('order_date', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Order Date')),
                ('ship_date', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Shipments Date')),
                ('expected_date', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date Expected Time')),
                ('arrival_date', models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Date Arrival Time')),
                ('description', models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Carrier',
                'verbose_name_plural': 'Carriers',
            },
        ),
        migrations.RemoveField(
            model_name='import',
            name='description',
        ),
        migrations.RemoveField(
            model_name='import',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='transportations',
            name='description',
        ),
        migrations.RemoveField(
            model_name='transportations',
            name='detailsForCarriers',
        ),
        migrations.AddField(
            model_name='import',
            name='date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='import',
            name='details',
            field=models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details'),
        ),
        migrations.AddField(
            model_name='import',
            name='paid_fact',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Paid Real'),
        ),
        migrations.AddField(
            model_name='import',
            name='paid_real',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Paid Real'),
        ),
        migrations.AddField(
            model_name='import',
            name='to_dealer',
            field=models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='To Dealer'),
        ),
        migrations.AddField(
            model_name='import',
            name='to_seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='to_seller', to='info.provider', verbose_name='To Seller'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='importproducts',
            name='Customs_costs_perc',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Customs Costs Perc'),
        ),
        migrations.AddField(
            model_name='importproducts',
            name='Customs_costs_price',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Customs Costs Price'),
        ),
        migrations.AddField(
            model_name='importproducts',
            name='price_fact',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Price Fact'),
        ),
        migrations.AddField(
            model_name='repo',
            name='fromCountry',
            field=models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='From Country'),
        ),
        migrations.AddField(
            model_name='repo',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='repo',
            name='toCountry',
            field=models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='To Country'),
        ),
        migrations.AddField(
            model_name='transportations',
            name='details',
            field=models.TextField(blank=True, default=None, max_length=155, null=True, verbose_name='Details'),
        ),
        migrations.AlterField(
            model_name='import',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='info.provider', verbose_name='Currency'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repo',
            name='repoDate',
            field=models.CharField(blank=True, default=None, max_length=155, null=True, verbose_name='Repository Start Date'),
        ),
        migrations.DeleteModel(
            name='Carriers',
        ),
        migrations.AddField(
            model_name='transportationunit',
            name='sellers',
            field=models.ManyToManyField(blank=True, to='finance.import', verbose_name='Sellers'),
        ),
        migrations.AddField(
            model_name='craftunit',
            name='expenses',
            field=models.ManyToManyField(blank=True, to='finance.craftunitexpenses', verbose_name='Expenses'),
        ),
        migrations.AlterField(
            model_name='salarycalc',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.salarycalcworker', verbose_name='Worker'),
        ),
        migrations.AlterField(
            model_name='transportations',
            name='Carriers',
            field=models.ManyToManyField(blank=True, to='finance.transportationunit', verbose_name='Carriers'),
        ),
    ]
