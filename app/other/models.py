import uuid as uuid
from django.db import models


class JobsDay(models.Model):
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
        verbose_name = 'JobDay'
        verbose_name_plural = 'JobsDay'

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


# class Workers(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#
#     isActive = models.BooleanField(
#         default=True,
#         null=True,
#         blank=True,
#         verbose_name="Active"
#     )
#
#     name = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Name"
#     )
#
#     phone = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Phone"
#     )
#
#     salary = models.FloatField(
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Salary"
#     )
#
#     details = models.TextField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Details"
#     )
#
#     date = models.DateField(
#         auto_now_add=True,
#         null=True,
#         blank=True,
#         verbose_name="Date"
#     )
#
#     created = models.DateTimeField(
#         auto_now_add=True,
#         null=True,
#         blank=True,
#         verbose_name="Created Date"
#     )
#
#     class Meta:
#         verbose_name = 'Worker'
#         verbose_name_plural = 'Workers'
#
#     def __str__(self):
#         return self.name
#
#
# class JobsInfo(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#
#     isActive = models.BooleanField(
#         default=True,
#         null=True,
#         blank=True,
#         verbose_name="Active"
#     )
#
#     JobName = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Job Name"
#     )
#
#     workers = models.ManyToManyField(
#         Workers,
#         blank=True,
#         verbose_name="Workers"
#     )
#
#     details = models.TextField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Details"
#     )
#
#     created = models.DateTimeField(
#         auto_now_add=True,
#         null=True,
#         blank=True,
#         verbose_name="Created Date"
#     )
#
#     class Meta:
#         verbose_name = 'JobInfo'
#         verbose_name_plural = 'JobsInfo'
#
#     def __str__(self):
#         return self.JobName
#
#
# class Jobs(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#
#     isActive = models.BooleanField(
#         default=True,
#         null=True,
#         blank=True,
#         verbose_name="Active"
#     )
#
#     client = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Client"
#     )
#
#     JobName = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Job Name"
#     )
#
#     details = models.TextField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Details"
#     )
#
#     date = models.DateField(
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Date"
#     )
#
#     phone = models.CharField(
#         max_length=155,
#         default=None,
#         null=True,
#         blank=True,
#         verbose_name="Phone"
#     )
#
#     data = models.ManyToManyField(
#         JobsInfo,
#         blank=False,
#         verbose_name="Data"
#     )
#
#     created = models.DateTimeField(
#         auto_now_add=True,
#         null=True,
#         blank=True,
#         verbose_name="Created Date"
#     )
#
#     class Meta:
#         verbose_name = 'Job'
#         verbose_name_plural = 'Jobs'
#
#     def __str__(self):
#         return self.client