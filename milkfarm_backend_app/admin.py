from django.contrib import admin
from milkfarm_backend_app.models import *
# from milkfarm_backend_app import TodaysData


class AdminMember(admin.ModelAdmin):
    list_display = ['member_id','name','phone','email','types']


class AdminTodaysData(admin.ModelAdmin):
    list_display = ['id','name','name_id','fat','snf','rate','lit']


# Register your models here.
admin.site.register(Member , AdminMember)
admin.site.register(TodaysData , AdminTodaysData)
admin.site.register(Payment)