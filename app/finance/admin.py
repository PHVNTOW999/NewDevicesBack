from django.contrib import admin

from . import models


@admin.register(models.UnitMeas)
class UnitMeasAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )


@admin.register(models.SalaryCalc)
class SalaryCalcAdmin(admin.ModelAdmin):
    list_display = (
        'worker',
        'date',
        'uuid'
    )


@admin.register(models.CompletedWorks)
class CompletedWorksAdmin(admin.ModelAdmin):
    list_display = (
        'work',
        'amount',
        'uuid'
    )


@admin.register(models.Import)
class ImportAdmin(admin.ModelAdmin):
    list_display = (
        'seller',
        'uuid'
    )


@admin.register(models.ImportProducts)
class ImportProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )


@admin.register(models.ImportFromArmenia)
class ImportFromArmeniaAdmin(admin.ModelAdmin):
    list_display = (
        'seller',
        'uuid'
    )


@admin.register(models.ImportProductsFromArmenia)
class ImportProductsFromArmeniaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'uuid'
    )


@admin.register(models.Carriers)
class CarriersAdmin(admin.ModelAdmin):
    list_display = (
        'fromCountry',
        'toCountry',
        'uuid'
    )


@admin.register(models.Transportations)
class TransportationsAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'uuid'
    )
