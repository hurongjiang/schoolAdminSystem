from django.shortcuts import render,redirect
from .forms import Schoolroolform,Familymemberoneform,Familymembertwoform,Alterstudentinfo
from .models import Schoolrool,Familymemberone,Familymembertwo
from public.models import School,Grade,Class_bj
from .dowload_model import export_st_info_excel,export_class_info_excel,export_grade_info_excel
import datetime
# Create your views here.

def login(request):
    context = {}
    return render(request,'login/index.html')

def is_family_register(request):
    return render(request,'register/is_family_register.html')

def student_register(request):
    context = {}
    if request.method == 'POST':
        IDcard = request.POST.get('IDcard')
        if not Schoolrool.objects.filter(IDcard=IDcard).exists():
            schoolroolform = Schoolroolform(request.POST)
            schoolroolform.save()
            st_pk = Schoolrool.objects.get(IDcard=IDcard)
            request.session['st_pk'] = st_pk.pk
            return redirect(family_register)
        else:
            try:
                st_pk = Schoolrool.objects.get(IDcard=IDcard)
                st_pk.familymemberone
                context['errors'] = '你输入的学生信息已存在！！'
            except Exception as e:
                context['errors'] = '你输入的学生信息已存在,但家庭信息没有输入'
                return redirect(family_register)
    context['schoolroolform'] = Schoolroolform()
    return render(request,'register/student_register.html',context)

def single_student_register(request):
    context = {}
    if request.method == 'POST':
        IDcard = request.POST.get('IDcard')
        if not Schoolrool.objects.filter(IDcard=IDcard).exists():
            schoolroolform = Schoolroolform(request.POST)
            schoolroolform.save()
            st_pk = Schoolrool.objects.get(IDcard=IDcard)
            request.session['st_pk'] = st_pk.pk
            return redirect(single_parent_family)
        else:
            try:
                st_pk = Schoolrool.objects.get(IDcard=IDcard)
                st_pk.familymemberone
                context['errors'] = '你输入的学生信息已存在！！'
            except Exception as e:
                context['errors'] = '你输入的学生信息已存在,但家庭信息没有输入'
                return redirect(family_register)
    context['schoolroolform'] = Schoolroolform()
    return render(request,'register/single_student_register.html',context)

def family_register(request):
    context = {}
    if request.method == 'POST':
        st_pk = request.session.get('st_pk')
        st_info = Schoolrool.objects.get(pk=st_pk)
        if not Familymemberone.objects.filter(name=st_info).exists():
            familymemberoneform = Familymemberoneform(request.POST,instance = Familymemberone(name = st_info))
            familymembertwoform = Familymembertwoform(request.POST,instance = Familymembertwo(name = st_info))
            familymemberoneform.save()
            familymembertwoform.save()
            return redirect(register_success)
        else:
            context['errors'] = '你输入的家庭信息已存在！！'
            return redirect(register_success)
    context['familymemberoneform']=Familymemberoneform()
    context['familymembertwoform']=Familymembertwoform()
    return render(request,'register/family_register.html',context)

def single_parent_family(request):
    context = {}
    if request.method == 'POST':
        st_pk = request.session.get('st_pk')
        st_info = Schoolrool.objects.get(pk=st_pk)
        if not Familymemberone.objects.filter(name=st_info).exists():
            familymemberoneform = Familymemberoneform(request.POST,instance = Familymemberone(name = st_info))
            familymemberoneform.save()
            return redirect(register_success)
        else:
            context['errors'] = '你输入的家庭信息已存在！！'
            return redirect(register_success)
    context['familymemberoneform']=Familymemberoneform()
    return render(request,'register/single_family_register.html',context)

def register_success(request):
    return render(request,'register/register_success.html')

def grade_class_public(request):
    context={}
    context['grade'] = Grade.objects.all().values('grade')
    context['class_bj'] = Class_bj.objects.all().values('class_bj')
    return render(request,'dowload_info/dowload_st_info.html',context)

def dowlaod_st_info(request):
    if request.method == 'POST':
        username = request.user.username
        if username == 'hrj':
            schoolrool = Schoolrool.objects.all()
            if schoolrool.exists():
                return export_class_info_excel(request,schoolrool)
        elif School.objects.filter(school=username).exists():
            return export_st_info_excel(request,username)
        else:
            return redirect('user_login')
    return grade_class_public(request)

def dowload_bj_st_info(request):
    if request.method == 'POST':
        grade=request.POST.get('grade')
        class_bj = request.POST.get('class_bj')
        grade = Grade.objects.filter(grade=grade).first()
        class_bj = Class_bj.objects.filter(class_bj=class_bj).first()
        school = School.objects.filter(school=request.user.username)
        if school.exists():
            schoolrool=school.first().schoolrool_set.filter(grade=grade,class_bj=class_bj)
            if schoolrool.exists():
                return export_class_info_excel(request,schoolrool)
    return grade_class_public(request)

def dowload_grade_st_info(request):
    if request.method == 'POST':
        grade = request.POST.get('grade')
        grade = Grade.objects.filter(grade=grade).first()
        school = School.objects.filter(school=request.user.username)
        if school.exists():
            st_info=school.first().schoolrool_set.filter(grade=grade)
            if st_info.exists():
                return export_grade_info_excel(request,st_info)
    return grade_class_public(request)

def show_st_info(request):
    context ={}
    school = School.objects.filter(school=request.user.username)
    for school_tem in school:
        st_info = school_tem.schoolrool_set.all()
        st_total = []
        for st_tem in st_info:
            
            try:
                familymemberone = st_tem.familymemberone
            except Exception as e:
                familymemberone={}
                familymemberone['member_name_one'] = '无'
            try:
                familymembertwo = st_tem.familymembertwo
            except Exception as e:
                familymembertwo={}
                familymembertwo['member_name_two'] = '无'
            context_tem = {}
            context_tem['st_tem'] = st_tem
            context_tem['familymemberone'] = familymemberone
            context_tem['familymembertwo'] = familymembertwo
            st_total.append(context_tem)
        context['st_all_info'] = st_total
    return render(request,'show_student/show_st_info.html',context)

def show_one_st(request):
    context ={}
    if request.method == 'POST':
        alterstudentinfo=Alterstudentinfo(request.POST)
        if alterstudentinfo.is_valid():
            IDcard = alterstudentinfo.cleaned_data['IDcard']
            schoolrool = Schoolrool.objects.filter(IDcard=IDcard)
            if schoolrool.exists():
                context['schoolrool'] = schoolrool.first()
                return render(request,'show_student/show_one_st_info.html',context)
            else:
                context['errors'] = '该学生的学籍不存在！请先注册！'
    context['alterstudentinfo']=Alterstudentinfo()
    return render(request,'show_student/show_one_st.html',context)

def alter_st_info(request):
    context ={}
    if request.method == 'POST':
        alterstudentinfo=Alterstudentinfo(request.POST)
        if alterstudentinfo.is_valid():
            IDcard =alterstudentinfo.cleaned_data['IDcard']
            schoolrool = Schoolrool.objects.get(IDcard=IDcard)
            try:
                familymemberone = schoolrool.familymemberone
                familymemberone = Familymemberoneform(instance=familymemberone)
                context['familymemberone'] = familymemberone
                familymembertwo = schoolrool.familymembertwo
                familymembertwo = Familymembertwoform(instance=familymembertwo)
                context['familymembertwo'] = familymembertwo
            except Exception as e:
                print(e)
            schoolrool = Schoolroolform(instance=schoolrool)
            context['schoolrool'] = schoolrool
            return render(request,'register/alter_st_info.html',context)
    context['alterstudentinfo'] = Alterstudentinfo()
    return render(request,'register/input_idcard.html',context)

#学生信息修改后保存
def alter_st_success(request):
    context ={}
    if request.method == 'POST':
        IDcard = request.POST['IDcard']
        schoolrool_tem = Schoolrool.objects.get(IDcard=IDcard)
        schoolrool = Schoolroolform(request.POST,instance=schoolrool_tem).save()
        try:
            fone = schoolrool.familymemberone
            Familymemberoneform(request.POST,instance=fone).save()
            ftwo = schoolrool.familymembertwo
            familymembertwo = Familymembertwoform(request.POST,instance=ftwo).save()
        except Exception as e:
            print(e)
    context['alterstudentinfo'] = Alterstudentinfo()
    return render(request,'register/alter_st_info.html',context)
