import uuid as uuid
from django.db import models

from app.finance.models import UnitMeas


# # Единица измерения
# class UnitMeas(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#
#     name = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Name"
#     )
#
#     class Meta:
#         verbose_name = 'Unit measurements'
#         verbose_name_plural = 'Unit measurements'
#
#     def __str__(self):
#         return self.name


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
        return self.name


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

    details = models.TextField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Details"
    )

    price_sell = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount AMD"
    )

    amount_amd = models.FloatField(
        default=None,
        null=True,
        blank=True,
        verbose_name="Amount AMD"
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

    client = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
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
        verbose_name="Carriers"
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
        return self.client


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

    client = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
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

    JobName = models.CharField(
        max_length=155,
        default=None,
        null=True,
        blank=True,
        verbose_name="Job Name"
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

    data = models.ManyToManyField(
        JobsInfo,
        blank=False,
        verbose_name="Data"
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
