from django.contrib import admin

from . import models


@admin.register(models.Meet)
class MeetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'datetime',
        'uuid'
    )


@admin.register(models.OfferUnit)
class OfferUnitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'datetime',
        'uuid'
    )


@admin.register(models.Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'datetime',
        'uuid'
    )


@admin.register(models.Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'datetime',
        'uuid'
    )


@admin.register(models.Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'uuid'
    )


@admin.register(models.Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'uuid'
    )


@admin.register(models.Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'uuid'
    )


@admin.register(models.Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'uuid'
    )


@admin.register(models.JobsInfo)
class JobsInfoAdmin(admin.ModelAdmin):
    list_display = (
        'JobName',
        'uuid'
    )