''''''

'''
存放所有的类
学校、学员、课程、讲师、管理员
'''


from db import db_handler

class Base:
    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls,username):
        obj = db_handler.select(cls,username)

        # obj可能是None或者一个对象
        return obj

class Admin(Base):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def create_school(self,school_name,school_addr):
        school_obj = School(school_name,school_addr)
        school_obj.save()

    def create_course(self,course_name,course_cycle,school_obj):

        # 创建课程对象并保存
        course_obj = Course(course_name,course_cycle)
        course_obj.save()

        # 更新学校对象信息
        school_obj.course_li.append(course_name)
        school_obj.save()

    def create_teacher(self,teacher_name,teacher_password):
        teacher_obj = Teacher(teacher_name,teacher_password)
        teacher_obj.save()



class School(Base):
    def __init__(self, school_name, school_addr):
        self.username = school_name
        self.addr = school_addr
        self.course_li = []

class Course(Base):
    def __init__(self,course_name,course_cycle):
        self.username = course_name
        self.cycle = course_cycle
        self.student_li = []

class Teacher(Base):
    def __init__(self,teacher_name,teacher_password):
        self.username = teacher_name
        self.password = teacher_password
        self.teacher_course_li = []

    def choice_course(self,course_name):
        self.teacher_course_li.append(course_name)
        self.save()

    def change_score(self,choice_student,score,choice_course):

        # 生成学生对象
        student_obj = Student.select(choice_student)

        # 更改学生对象课程分数列表中的课程分数
        student_obj.score[choice_course] = score

        # 对数据进行保存
        student_obj.save()





class Student(Base):
    def __init__(self,student_name,student_password):
        self.username = student_name
        self.password = student_password
        self.school = None
        self.course_li = []
        self.score = {} # {'课程名字'：分数}

    def choice_school(self,choice_school_name):
        self.school = choice_school_name
        self.save()

    def choice_course(self,choice_course_name):

        # 学生的课程列表绑定课程
        self.course_li.append(choice_course_name)
        self.save()

        # 课程的学生列表反向绑定学生
        course_obj = Course.select(choice_course_name)
        course_obj.student_li.append(self.username)
        course_obj.save()