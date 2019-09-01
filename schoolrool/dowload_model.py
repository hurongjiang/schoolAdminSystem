from django.shortcuts import render,HttpResponse
from django.utils.http import urlquote
from io import BytesIO
import xlwt,datetime

from public.models import School

#写入excel文件
def export_st_info_writer(request,type_data):
    xldata = xlwt.Workbook(encoding='utf8')
    sheet = xldata.add_sheet(type_data)
    style_heading = xlwt.easyxf("""
            font:
                name Arial,
                colour_index white,
                bold on,
                height 0xA0;
            align:
                wrap off,
                vert center,
                horiz center;
            pattern:
                pattern solid,
                fore-colour 0x19;
            borders:
                left THIN,
                right THIN,
                top THIN,
                bottom THIN;
            """)
    sheet.write(0,0,type_data)
    #表头
    sheet_data= ['姓名','曾用名','身份证号','性别','民族','学校','年级','班级','户口性质','现住地址','是否是独生子女','是否留守儿童','健康状况','入学方式','就读方式','是否残疾人','国网学籍号','省网学籍号']
    heald_nu = len(sheet_data)
    for i in range(0,len(sheet_data)):
        sheet.write(1,i,sheet_data[i],style_heading)
    sheet_data= ['成员1姓名','成员1关系','成员1地址','成员1电话','成员1是否监护人','成员1身份证号','成员1民族','成员1工作单位','成员1职务','成员2姓名','成员2关系','成员2地址','成员2电话','成员2是否监护人','成员2身份证号','成员2民族','成员2工作单位','成员2职务']
    for i in range(0,len(sheet_data)):
        sheet.write(1,i+heald_nu,sheet_data[i],style_heading)
    #学生基本信息
    sc_info = School.objects.get(school=type_data)
    st_info = sc_info.schoolrool_set.all()
    for st_tem,i in zip(st_info,range(0,len(st_info))):
        sheet.write(i+2,0,st_tem.name)
        sheet.write(i+2,1,st_tem.alread_name)
        sheet.write(i+2,2,st_tem.IDcard)
        sheet.write(i+2,3,st_tem.sex.sex)
        sheet.write(i+2,4,st_tem.nation.nation)
        sheet.write(i+2,5,st_tem.school.school)
        sheet.write(i+2,6,st_tem.grade.grade)
        sheet.write(i+2,7,st_tem.class_bj.class_bj)
        sheet.write(i+2,8,st_tem.by_type.bytype)
        sheet.write(i+2,9,st_tem.address)
        if st_tem.is_child:
            is_child = '是'
        else:
            is_child = '否'
        sheet.write(i+2,10,is_child)
        if st_tem.is_leftover_child:
            is_leftover_child = '是'
        else:
            is_leftover_child = '否'
        sheet.write(i+2,11,is_leftover_child)
        if st_tem.is_healdy:
            is_healdy = '是'
        else:
            is_healdy = '否'
        sheet.write(i+2,12,is_healdy)
        sheet.write(i+2,13,st_tem.entrance_go)
        sheet.write(i+2,14,st_tem.how_go_school)
        if st_tem.is_disable:
            is_disable = '是'
        else:
            is_disable = '否'
        sheet.write(i+2,15,is_disable)
        sheet.write(i+2,16,st_tem.country_ID)
        sheet.write(i+2,17,st_tem.province_ID)
        #学生家庭信息
        try:
            familyone = st_tem.familymemberone
            
            sheet.write(i+2,18,familyone.member_name_one)
            sheet.write(i+2,19,familyone.member_ralation_one.ralation)
            sheet.write(i+2,20,familyone.member_address_one)
            sheet.write(i+2,21,familyone.member_phone_one)
            if familyone.is_guardian_one:
                is_guardian = '是'
            else:
                is_guardian = '否'
            sheet.write(i+2,22,is_guardian)
            sheet.write(i+2,23,familyone.member_idcard_one)
            sheet.write(i+2,24,familyone.member_nation_one.nation)
            sheet.write(i+2,25,familyone.member_job_one)
            sheet.write(i+2,26,familyone.member_duty_one)

            try:
                familytwo = st_tem.familymembertwo
                sheet.write(i+2,27,familytwo.member_name_two)
                sheet.write(i+2,28,familytwo.member_ralation_two.ralation)
                sheet.write(i+2,29,familytwo.member_address_two)
                sheet.write(i+2,30,familytwo.member_phone_two)
                if familytwo.is_guardian_two:
                    is_guardian = '是'
                else:
                    is_guardian = '否'
                sheet.write(i+2,31,is_guardian)
                sheet.write(i+2,32,familytwo.member_idcard_two)
                sheet.write(i+2,33,familytwo.member_nation_two.nation)
                sheet.write(i+2,34,familytwo.member_job_two)
                sheet.write(i+2,35,familytwo.member_duty_two)
            except Exception as e:
                sheet.write(i+len(st_info)+2,1,'注：没有输入家庭信息成员2,第%s行%s'%(i+3,st_tem.name))
        except Exception as e:
            sheet.write(i+len(st_info)+2,0,'注：没有输入家庭信息成员1,第%s行%s'%(i+3,st_tem.name))

    output = BytesIO()
    xldata.save(output)
    # 重新定位到开始
    output.seek(0)
    return output


#读取试卷文件
def export_st_info_excel(request,type_data):
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    file_name = '%s学生信息%s'%(type_data,datetime.datetime.now())
    response['Content-Disposition'] = 'attachment;filename=%s.xls'%urlquote(file_name)
    output = export_st_info_writer(request,type_data)
    response.write(output.getvalue())
    return response   