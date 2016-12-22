from django.contrib import admin

from .models import Momo


@admin.register(Momo)
class AdminMomo(admin.ModelAdmin):
    list_display = ('name',)
