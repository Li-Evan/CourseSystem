from db import models


def register_interface(username, password):
    # 判断对象是否存在
    exist = models.Admin.select(username)
    # 存在则返回false
    if exist:
        return False, '用户名已存在!'

    # 不存在生成对象，保存并返回true
    admin_obj = models.Admin(username, password)
    admin_obj.save()
    return True, '注册成功！'


# def login_interface(username, password):
#     obj = models.Admin.select(username)
#
#     if not obj:
#         return False, '该用户未注册！'
#
#     else:
#         if obj.password == password:
#             return True, '登录成功！'
#         else:
#             return False, '密码错误！'


def create_school_interface(school_name, school_addr, admin_name):
    # 查看学校是否存在
    school_obj = models.School.select(school_name)
    # 存在则返回已经存在
    if school_obj:
        return False, '学校已经存在！'
    # 不存在则创建并保存
    else:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.create_school(school_name, school_addr)
        return True, f'{school_name}创建成功！'


def create_course_interface(admin_user, school_name, course_name, course_cycle):
    # 判断课程是否已经存在于学校课程列表中
    school_obj = models.School.select(school_name)
    school_course_li = school_obj.course_li

    # 若存在返回已经存在
    if course_name in school_course_li:
        return False, '课程已存在！'

    # 若不存在用管理员对象创建课程，并绑定到学校的课程列表下
    admin_obj = models.Admin.select(admin_user)
    admin_obj.create_course(course_name, course_cycle, school_obj)
    return True, f'[{course_name}]创建成功，绑定的学校是[{school_name}]'


def create_teacher_interface(teacher_name, admin_user, teacher_password='123'):
    # 判断老师对象是否存在
    teacher_obj = models.Teacher.select(teacher_name)

    # 存在则返回结果
    if teacher_obj:
        return False,'该老师已经存在！'

    # 不存在则进行创建
    admin_obj = models.Admin.select(admin_user)
    admin_obj.create_teacher(teacher_name,teacher_password)
    return True,f'[{teacher_name}]创建成功！'
