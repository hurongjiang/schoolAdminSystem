from django.forms import ModelForm
from .models import Schoolrool,Familymemberone,Familymembertwo

class Schoolroolform(ModelForm):
    class Meta:
        model = Schoolrool
        fields = '__all__'
        labels = {
        'name':'姓名',
        'alread_name':'曾用名',
        'sex':'性别',
        'IDcard':'身份证号',
        'nation':'民族',
        'school':'学校',
        'grade':'年级',
        'class_bj':'班级',
        'by_type':'户口性质',
        'address':'现住地址',
        'is_child':'是否是独生子女',
        'is_leftover_child':'是否留守儿童',
        'is_healdy':'健康状况',
        'entrance_date':'入学年月',
        'entrance_go':'入学方式',
        'how_go_school':'就读方式',
        'is_disable':'是否残疾人',
        'country_ID':'国网学籍号',
        'province_ID':'省网学籍号',
        }
    def clean(self):
        name = self.cleaned_data['name']
        print(1111)
        return self.cleaned_data
#['alread_name','name','sex','IDcard','nation','school','grade','class_bj','by_type','address','is_child','is_leftover_child','is_healdy','entrance_date','entrance_go','how_go_school','is_disable','country_ID','province_ID']
#['member_name_one','member_ralation_one','member_address_one','member_phone_one','is_guardian_one','member_Idcard_one','member_nation_one','member_job_one','member_duty_one']
#['member_name_two','member_ralation_two','member_address_two','member_phtwo_two','is_guardian_two','member_Idcard_two','member_nation_two','member_job_two','member_duty_two']

class Familymemberoneform(ModelForm):
    class Meta:
        model = Familymemberone
        exclude = ['name']
        labels ={
            'name':'姓名',
            'member_name_one':'成员1姓名',
            'member_ralation_one':'成员1关系',
            'member_address_one':'成员1地址',
            'member_phone_one':'成员1电话',
            'is_guardian_one':'成员1是否监护人',
            'member_idcard_one':'成员1身份证号',
            'member_nation_one':'成员1民族',
            'member_job_one':'成员1工作单位',
            'member_duty_one':'成员1职务',
        }

class Familymembertwoform(ModelForm):
    class Meta:
        model = Familymembertwo
        exclude = ['name']

        labels ={
            'name':'姓名',
            'member_name_two':'成员2姓名',
            'member_ralation_two':'成员2关系',
            'member_address_two':'成员2地址',
            'member_phone_two':'成员2电话',
            'is_guardian_two':'成员2是否监护人',
            'member_idcard_two':'成员2身份证号',
            'member_nation_two':'成员2民族',
            'member_job_two':'成员2工作单位',
            'member_duty_two':'成员2职务',
        }