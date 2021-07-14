from django.contrib import admin
from .models import *


class LegInline(admin.StackedInline):
    model = Leg


class TourAdmin(admin.ModelAdmin):
    inlines = [LegInline]


admin.site.register(Tour, TourAdmin)
admin.site.register(Leg)
