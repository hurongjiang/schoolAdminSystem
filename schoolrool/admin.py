from django.contrib import admin
from .models import Schoolrool,Familymemberone,Familymembertwo
# Register your models here.
@admin.register(Schoolrool)
class SchoolroolAdmin(admin.ModelAdmin):
    list_display = ['id','alread_name','name','sex','IDcard','nation','school','grade','class_bj','by_type','address','is_child','is_leftover_child','is_healdy','entrance_date','entrance_go','how_go_school','is_disable','country_ID','province_ID']

@admin.register(Familymemberone)
class FamilymemberoneAdmin(admin.ModelAdmin):
    list_display = ['id','name','member_name_one','member_ralation_one','member_address_one','member_phone_one','is_guardian_one','member_idcard_one','member_nation_one','member_job_one','member_duty_one']

@admin.register(Familymembertwo)
class FamilymembertwoAdmin(admin.ModelAdmin):
    list_display = ['id','name','member_name_two','member_ralation_two','member_address_two','member_phone_two','is_guardian_two','member_idcard_two','member_nation_two','member_job_two','member_duty_two']