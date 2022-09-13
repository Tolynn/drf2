from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category, Women


# Register your models here.
@admin.register(Women)
class Women(ModelAdmin):
    pass


@admin.register(Category)
class Category(ModelAdmin):
    pass