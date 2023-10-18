from django.contrib import admin

from . import models


@admin.register(models.JobsDay)
class JobsDayAdmin(admin.ModelAdmin):
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


# @admin.register(models.Jobs)
# class JobsAdmin(admin.ModelAdmin):
#     list_display = (
#         'client',
#         'uuid'
#     )
#
#
# @admin.register(models.JobsInfo)
# class JobsInfoAdmin(admin.ModelAdmin):
#     list_display = (
#         'JobName',
#         'uuid'
#     )
#
#
# @admin.register(models.Workers)
# class WorkersAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'uuid'
#     )
