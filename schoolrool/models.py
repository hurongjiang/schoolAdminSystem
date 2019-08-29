from django.db import models
from public.models import Sex,Nation,Bytype,Ralation,School,Grade,Class_bj

# Create your models here.
class Schoolrool(models.Model):
    name = models.CharField(max_length=15)
    alread_name = models.CharField(max_length=15,default='无')
    IDcard = models.CharField(max_length=18)
    sex = models.ForeignKey(Sex,on_delete=models.DO_NOTHING)
    nation = models.ForeignKey(Nation,on_delete=models.DO_NOTHING)
    school = models.ForeignKey(School,on_delete = models.DO_NOTHING)
    grade = models.ForeignKey(Grade,on_delete=models.DO_NOTHING)
    class_bj = models.ForeignKey(Class_bj,on_delete=models.DO_NOTHING)
    by_type = models.ForeignKey(Bytype,on_delete= models.DO_NOTHING)
    address = models.CharField(max_length=150)
    is_child = models.BooleanField(default=False)
    is_leftover_child = models.BooleanField(default=False)
    is_healdy = models.BooleanField(default=True)
    entrance_date = models.DateTimeField(auto_now_add =True)
    entrance_go = models.CharField(max_length=150)
    how_go_school = models.CharField(max_length=150)
    is_disable = models.BooleanField(default=False)
    country_ID = models.CharField(max_length=20,default='',blank=True)
    province_ID = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return '<schoolrool>:%s'%self.name
    

class Familymemberone(models.Model):
    name = models.OneToOneField(Schoolrool,on_delete=models.DO_NOTHING)
    member_name_one = models.CharField(max_length=15)
    member_ralation_one = models.ForeignKey(Ralation,on_delete=models.DO_NOTHING)
    member_address_one = models.CharField(max_length=150)
    member_phone_one = models.CharField(max_length=11)
    is_guardian_one = models.BooleanField(default=True)
    member_idcard_one = models.CharField(max_length=18)
    member_nation_one = models.ForeignKey(Nation,on_delete=models.DO_NOTHING)
    member_job_one = models.CharField(max_length=150)
    member_duty_one = models.CharField(max_length=150)

    def __str__(self):
        return '<Familymemberone>:%s'%self.member_name_one

class Familymembertwo(models.Model):
    name = models.OneToOneField(Schoolrool,on_delete=models.DO_NOTHING)
    member_name_two = models.CharField(max_length=15)
    member_ralation_two = models.ForeignKey(Ralation,on_delete=models.DO_NOTHING)
    member_address_two = models.CharField(max_length=150)
    member_phone_two = models.CharField(max_length=11)
    is_guardian_two = models.BooleanField(default=True)
    member_idcard_two = models.CharField(max_length=18)
    member_nation_two = models.ForeignKey(Nation,on_delete=models.DO_NOTHING)
    member_job_two = models.CharField(max_length=150)
    member_duty_two = models.CharField(max_length=150)

    def __str__(self):
        return '<Familymembertwo>:%s'%self.member_name_two