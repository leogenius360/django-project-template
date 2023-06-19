from django.contrib import admin

from hello_world.models import VisitCounter

# Register your models here.

@admin.register(VisitCounter)
class VisitCounterAdmin(admin.ModelAdmin):
  pass

