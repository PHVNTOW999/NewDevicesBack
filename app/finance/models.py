import uuid as uuid
from django.db import models

from info.models import Workers, Provider


# Единица измерения
class UnitMeas(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    class Meta:
        verbose_name = 'Unit measurements'
        verbose_name_plural = 'Unit measurements'

    def __str__(self):
        return self.name


# Завершенные работы
class CompletedWorks(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    worker = models.ForeignKey(
        Workers,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Worker"
    )

    work = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Work desc"
    )

    amount = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount"
    )

    # curr

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'CompletedWork'
        verbose_name_plural = 'CompletedWorks'

    def __str__(self):
        return self.work


class CraftUnitExpenses(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    quantity = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Quantity"
    )

    price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Price"
    )

    date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Order Date"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Craft Unit Expenses'
        verbose_name_plural = 'Craft Units Expenses'

    def __str__(self):
        return self.name


class CraftUnit(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    date_start = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date Start"
    )

    quantity = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Quantity"
    )

    price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Price"
    )

    date_expected = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date Challenge"
    )

    date_end = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date End"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    expenses = models.ManyToManyField(
        CraftUnitExpenses,
        blank=True,
        verbose_name="Expenses"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'CraftUnit'
        verbose_name_plural = 'CraftUnits'

    def __str__(self):
        return self.name


# Разработка
class Craft(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    date_start = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date Start"
    )

    date_challenge = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date Challenge"
    )

    date_end = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date End"
    )

    sell_retail_price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Sell Retail Price"
    )

    sell_retail_perc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Sell Retail Percent"
    )

    sell_wholesale_price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Sell Wholesale Price"
    )

    sell_wholesale_perc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Sell Wholesale Percent"
    )

    rent_retail_price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Rent Retail Price"
    )

    rent_retail_perc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Rent Retail Percent"
    )

    rent_wholesale_price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Rent Wholesale Price"
    )

    rent_wholesale_perc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Rent Wholesale Percent"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Craft'
        verbose_name_plural = 'Crafts'

    def __str__(self):
        return self.name


# Импорт Связаных продуктов из Армении
class ImportProductsFromArmenia(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    unitMeas = models.ForeignKey(
        UnitMeas,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="UnitMeas"
    )

    quantity = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Quantity"
    )

    price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Price"
    )

    wholesalePrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Wholesale price"
    )

    percentSellingPrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Percent Selling Price"
    )

    totalSellingPrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Selling Price"
    )

    income = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Income"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )

    class Meta:
        verbose_name = 'ImportProductFromArmenia'
        verbose_name_plural = 'ImportProductsFromArmenia'

    def __str__(self):
        return self.name


# Импорт из Армении
class ImportFromArmenia(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    seller = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Seller"
    )

    phone = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Phone"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    products = models.ManyToManyField(
        ImportProductsFromArmenia,
        blank=True,
        verbose_name="Products"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )

    class Meta:
        verbose_name = 'ImportFromArmenia'
        verbose_name_plural = 'ImportFromArmenia'

    def __str__(self):
        return self.seller


class Currency(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Currency"
    )

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name


class Country(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    fromCountry = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="From Country"
    )

    toCountry = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="To Country"
    )

    amount = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount"
    )

    curr = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Currency"
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.fromCountry


# Импорт продуктов
class ImportProducts(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    unitMeas = models.ForeignKey(
        UnitMeas,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="UnitMeas"
    )

    quantity = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Quantity"
    )

    price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Price"
    )

    price_fact = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Price Fact"
    )

    currency = models.ForeignKey(
        Currency,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name="Currency"
    )

    # orderDate = models.DateField(
    #     default=None,
    #     null=True,
    #     blank=True,
    #     verbose_name="Order Date"
    # )

    # shipmentDate = models.DateField(
    #     default=None,
    #     null=True,
    #     blank=True,
    #     verbose_name="Shipment Date"
    # )

    totalWeight = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Total Weight"
    )

    weightNeto = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Neto Weight"
    )

    weightBrutto = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Brutto Weight"
    )

    Customs_costs_price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Customs Costs Price"
    )

    Customs_costs_perc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Customs Costs Perc"
    )

    bankExpensesCurr = models.ForeignKey(
        Currency,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="bank_expenses_currency",
        verbose_name="Bank Expenses Currency"
    )

    percentCustomsCosts = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Percent Customs Costs"
    )

    percentCustomsPrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Percent Customs Price"
    )

    bankExpensesAmount = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Bank Expenses Amount"
    )

    bankExpensesPerc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Bank Expenses Percent"
    )

    bankExpensesDays = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Bank Expenses Days"
    )

    costPrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Cost Price"
    )

    wholesalePerc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Wholesale Percent"
    )

    wholesalePrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Wholesale Price"
    )

    retailPerc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Retail Percent"
    )

    retailPrice = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Retail Price"
    )

    incomeFromWholesale = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Income From Wholesale"
    )

    incomeFromRetail = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Income From Retail"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )

    class Meta:
        verbose_name = 'ImportProduct'
        verbose_name_plural = 'ImportProducts'

    def __str__(self):
        return self.name


# Продукт
class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )


# Импорт
class Import(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    seller = models.ForeignKey(
        Provider,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Currency"
    )

    paid_real = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Paid Real"
    )

    paid_fact = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Paid Real"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    to_dealer = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="To Dealer"
    )

    to_seller = models.ForeignKey(
        Provider,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="to_seller",
        verbose_name="To Seller"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    products = models.ManyToManyField(
        ImportProducts,
        blank=True,
        verbose_name="Products"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )

    class Meta:
        verbose_name = 'Import'
        verbose_name_plural = 'Imports'

    def __str__(self):
        return self.seller


# Склад
class Repo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    carrier = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Carrier"
    )

    phone = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Phone"
    )

    fromCountry = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="From Country"
    )

    toCountry = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="To Country"
    )

    amount = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount"
    )

    curr = models.ForeignKey(
        Currency,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Currency"
    )

    repoName = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Repository Name"
    )

    repoDate = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Repository Start Date"
    )

    repoExpectedTime = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Repository Expected Time"
    )

    repoArrivalTime = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Repository Arrival Time"
    )

    class Meta:
        verbose_name = 'Repo'
        verbose_name_plural = 'Repos'

    def __str__(self):
        return self.carrier


# Перевозчики
class TransportationUnit(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    sellers = models.ManyToManyField(
        Import,
        blank=True,
        verbose_name="Sellers"
    )

    order_date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Order Date"
    )

    ship_date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Shipments Date"
    )

    expected_date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date Expected Time"
    )

    arrival_date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Date Arrival Time"
    )

    description = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Description"
    )

    class Meta:
        verbose_name = 'Carrier'
        verbose_name_plural = 'Carriers'

    def __str__(self):
        return f'{self.sellers}'


# Перевозка
class Transportations(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    Carriers = models.ManyToManyField(
        TransportationUnit,
        blank=True,
        verbose_name="Carriers"
    )

    class Meta:
        verbose_name = 'Transportation'
        verbose_name_plural = 'transportations'

    def __str__(self):
        return f'{self.no}'


# Расчет зарплаты по сотрудникам
class SalaryCalcWorker(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    worker = models.ForeignKey(
        Workers,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Worker"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'SalaryCalc'
        verbose_name_plural = 'SalaryCalc'

    def __str__(self):
        return f'{self.worker}'


# Расчет зарплаты по дням
class SalaryCalc(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    worker = models.ForeignKey(
        SalaryCalcWorker,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Worker"
    )

    no = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name="No"
    )

    date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date"
    )

    time_start_work = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Time Start Work"
    )

    time_end_work = models.TimeField(
        null=True,
        blank=True,
        verbose_name="Time Start Work"
    )

    CompletedWorks = models.ManyToManyField(
        CompletedWorks,
        blank=True,
        verbose_name="Completed Works"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'SalaryCalc'
        verbose_name_plural = 'SalaryCalc'

    def __str__(self):
        return f'{self.worker}'
