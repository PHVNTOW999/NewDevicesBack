import uuid as uuid
from django.db import models


class Phone(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)

    num = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Numbers"
    )

    desc = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Desc"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        ordering = ['created']

    def __str__(self):
        return f'{self.num}'


class Email(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Email"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.name


class CommunicationMethod(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True)

    phones = models.ManyToManyField(
        Phone,
        blank=True,
        verbose_name="Phones"
    )

    emails = models.ManyToManyField(
        Email,
        blank=True,
        verbose_name="Emails"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'CommunicationMethod'
        verbose_name_plural = 'CommunicationMethods'

    def __str__(self):
        return f'{self.phones} - {self.emails}'


# Клиент
class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=False,
        blank=False,
        verbose_name="Name"
    )

    desc = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Desc"
    )

    phone = models.ManyToManyField(
        Phone,
        blank=True,
        verbose_name="Phones"
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
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name


# Встречи
class Meet(models.Model):
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

    client = models.ForeignKey(
        Client,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="Client",
        verbose_name="Client"
    )

    datetime = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Datetime"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    phones = models.ManyToManyField(
        Phone,
        blank=True,
        verbose_name="phones"
    )

    emails = models.ManyToManyField(
        Email,
        blank=True,
        verbose_name="Emails"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )

    class Meta:
        verbose_name = 'Meet'
        verbose_name_plural = 'Meets'

    def __str__(self):
        return f'{self.client} - {self.created}'


class OfferUnit(models.Model):
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

    datetime = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Datetime"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    desc = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Desc"
    )

    unitMeas = models.ForeignKey(
        'finance.UnitMeas',
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

    price_sell_usd = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Price (Sell in USD)"
    )

    amount_usd = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount (USD)"
    )

    expenses_price = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Expenses Price"
    )

    expenses_other = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Expenses Other"
    )

    expenses_shipping = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Expenses shipping"
    )

    income_from_sales_perc = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Income from sales (Percent)"
    )

    income_from_sales_usd = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Income from sales (USD)"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    class Meta:
        verbose_name = 'Offer Unit'
        verbose_name_plural = 'Offer Units'

    def __str__(self):
        return self.name


class Offers(models.Model):
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

    client = models.ForeignKey(
        Client,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Client"
    )

    datetime = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Datetime"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    offer_unit = models.ManyToManyField(
        OfferUnit,
        blank=True,
        verbose_name="Offer Unit"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created date"
    )

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    def __str__(self):
        return f'${self.client}'


class Orders(models.Model):
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

    client = models.ForeignKey(
        Client,
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        verbose_name="Client"
    )

    phone = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Phone"
    )

    datetime = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Datetime"
    )

    amount_usd = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount USD"
    )

    order_date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Order Date"
    )

    task_date = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Task Date"
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
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.client


class Notes(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    desc = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Desc"
    )

    phone = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Phone"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
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
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.name


class Expenses(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
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
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.name


class Workers(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    name = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Name"
    )

    phone = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Phone"
    )

    salary = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Salary"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    date = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return self.name


class JobsInfo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    JobName = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Job Name"
    )

    workers = models.ManyToManyField(
        Workers,
        blank=True,
        verbose_name="Workers"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'JobInfo'
        verbose_name_plural = 'JobsInfo'

    def __str__(self):
        return self.JobName


class Jobs(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    client = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Client"
    )

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    phone = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Phone"
    )

    jobInfo = models.ManyToManyField(
        JobsInfo,
        blank=False,
        verbose_name="jobInfo"
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.client


class Provider(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    isActive = models.BooleanField(
        default=True,
        null=True,
        blank=True,
        verbose_name="Active"
    )

    Contact_person = models.CharField(
        max_length=155,
        default=None,
        null=False,
        blank=False,
        verbose_name="Contact Person"
    )

    Firm = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Firm"
    )

    desc = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Desc"
    )

    phone = models.ManyToManyField(
        Phone,
        blank=True,
        verbose_name="Phones"
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
        verbose_name="Created Date"
    )

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        return self.Contact_person
