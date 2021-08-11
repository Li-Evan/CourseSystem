import os
from conf import settings
from db import models


# 查看所有学校
def get_all_school_interface():
    school_obj_file_path = os.path.join(
        settings.DB_PATH, 'School'
    )

    if not os.path.exists(school_obj_file_path):
        return False, '请先联系管理员创建学校！'

    else:
        school_li = os.listdir(school_obj_file_path)
        return True, school_li


# 公共登录方法接口
def login_interface(username, password, user_type):
    obj = None
    if user_type == 'admin':
        obj = models.Admin.select(username)
    elif user_type == 'student':
        obj = models.Student.select(username)
    elif user_type == 'teacher':
        obj = models.Teacher.select(username)

    if not obj:
        return False, '该用户未注册！'

    else:
        if obj.password == password:
            return True, '登录成功！'
        else:
            return False, '密码错误！'


# 查看某个学校下面所有课程接口
def get_all_course_interface(school_name):

    school_obj = models.School.select(school_name)
    school_course_li = school_obj.course_li

    if not school_course_li:
        return False, '该学校暂未设置课程！'

    return True, school_course_li
