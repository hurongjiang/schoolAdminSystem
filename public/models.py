from django.db import models

# Create your models here.
class Sex(models.Model):
    sex = models.CharField(max_length=2)
    #True为男，False为女

    def __str__(self):
        return '<sex>:%s'%self.sex

class Nation(models.Model):
    nation = models.CharField(max_length=16)
    def __str__(self):
        return '<nation>:%s'%self.nation

class Bytype(models.Model):
    bytype = models.CharField(max_length=16)
#True为农业户口，False为非农业户口
    def __str__(self):
        return '<bytype>:%s'%self.bytype

class Ralation(models.Model):
    ralation = models.CharField(max_length=16)
    def __str__(self):
        return '<ralation>:%s'%self.ralation

class School(models.Model):
    school = models.CharField(max_length=150)

    def __str__(self):
        return '<school>:%s'%self.school

class Grade(models.Model):
    grade = models.CharField(max_length=6)
    #一到六年级
    def __str__(self):
        return '<grade>:%s'%self.grade

class Class_bj(models.Model):
    class_bj = models.CharField(max_length=6)
    #1到6班
    def __str__(self):
        return '<class_bj>:%s'%self.class_bj