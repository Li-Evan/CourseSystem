from db import models


def regester_interface(student_name, student_password):
    # 查看学生对象是否已经存在，若存在返回已存在
    student_obj = models.Student.select(student_name)

    if student_obj:
        return False, '用户已存在！'

    # 若不存在进行创建
    student_obj = models.Student(student_name, student_password)
    student_obj.save()
    return True, '注册成功！'


def choice_school_interface(choice_school_name, student_user):
    # 先判断该学生是否已经选择学校
    student_obj = models.Student.select(student_user)

    # 如果选择，返回已经选择
    if student_obj.school:
        return '该学生已经选择过学校了！'

    # 如果未选择，进行选择并保存更新后的数据
    student_obj.choice_school(choice_school_name)
    return f'绑定[{choice_school_name}]成功！'


def get_all_course_interface(student_name):

    student_obj = models.Student.select(student_name)
    school_name = student_obj.school

    if not school_name:
        return False,'尚未绑定学校，请先进行学校绑定！'

    school_obj = models.School.select(school_name)

    if not school_obj.course_li:
        return False,'请先联系管理员添加课程!'

    return True,school_obj.course_li


def choice_course_interface(choice_course_name,student_user):

    # 查看选择的课程是否已经在该学生课程列表中
    student_obj = models.Student.select(student_user)
    exist_course_li = student_obj.course_li

    # 若存在返回已经存在
    if choice_course_name in exist_course_li:
        return False,'课程已选择！'

    # 若不存在进行保存及数据更新
    student_obj.choice_course(choice_course_name)
    return True,'课程选择成功!'


def check_score_interface(student_name):

    student_obj = models.Student.select(student_name)
    score_dic = student_obj.score

    if score_dic:
        return True,score_dic
    else:
        return False,'尚未选择课程！'