from django.contrib import admin

from blog.models import Momo


@admin.register(Momo)
class AdminMomo(admin.ModelAdmin):
    list_display = ('name',)
