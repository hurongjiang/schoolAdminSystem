from django.shortcuts import render,redirect
from .forms import Schoolroolform,Familymemberoneform,Familymembertwoform
from .models import Schoolrool,Familymemberone,Familymembertwo
from public.models import School
from .dowload_model import export_st_info_excel
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

def dowlaod_st_info(request):
    context={}
    
    if request.method == 'POST':
        school_name = request.POST.get("school_name")
        return export_st_info_excel(request,school_name)
    return render(request,'dowload_info/dowload_st_info.html',context)