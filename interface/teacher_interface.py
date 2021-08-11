from db import models

def check_teach_course(teacher_name):

    teacher_obj = models.Teacher.select(teacher_name)
    teach_course_li = teacher_obj.teacher_course_li
    if not teach_course_li:
        return False,'该老师尚未选择任何课程'

    return True,teach_course_li

def choice_teach_course_interface(choice_course,teacher_user):

    # 创建老师对象
    teacher_obj = models.Teacher.select(teacher_user)

    # 如果老师已经选择该课程，返回已经选择
    if choice_course in teacher_obj.teacher_course_li:
        return False,'该课程已添加入课程列表中！'

    # 如果老师未选择该课程，将课程添加到老师对象的列表中并更新数据
    teacher_obj.choice_course(choice_course)
    return True,'添加成功！'

def show_course_student(choice_course):

    course_obj = models.Course.select(choice_course)
    course_student_li = course_obj.student_li

    if not course_student_li:
        return False,'暂无学生选择该门课程!'

    return True,course_student_li

def change_score_interface(teacher_user,choice_student,score,choice_course):

    # 生成老师对象
    teacher_obj = models.Teacher.select(teacher_user)

    # 使用老师对象中的修改分数方法进行分数修改
    teacher_obj.change_score(choice_student,score,choice_course)

    return '修改分数成功!'