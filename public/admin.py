from django.contrib import admin
from .models import Sex,Nation,Bytype,Ralation,School,Grade,Class_bj

# Register your models here.
@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ['id','sex']

@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ['id','nation']

@admin.register(Bytype)
class BytypeAdmin(admin.ModelAdmin):
    list_display = ['id','bytype']

@admin.register(Ralation)
class RalationAdmin(admin.ModelAdmin):
    list_display = ['id','ralation']

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id','school']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id','grade']

@admin.register(Class_bj)
class Class_bjAdmin(admin.ModelAdmin):
    list_display = ['id','class_bj']


