from interface import teacher_interface
from lib import common,common_interface

teacher_user = None


def login():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码:')

        flag,msg = common_interface.login_interface(
            username,password,user_type='teacher'
        )
        if flag:
            print(msg)
            global teacher_user
            teacher_user = username
            break
        else:
            print(msg)
            continue

@common.auth('teacher')
def check_teach_course():
    flag,msg_or_li = teacher_interface.check_teach_course(
        teacher_user
    )
    if not flag:
        print(msg_or_li)

    else:
        for index,course_name in enumerate(msg_or_li):
            print(f'编号{index}:{course_name}')

@common.auth('teacher')
def choice_teach_course():
    while True:

        # 打印学校列表
        flag,school_li = common_interface.get_all_school_interface()
        if not flag:
            print(school_li)
            break

        for index,school_name in enumerate(school_li):
            print(f'编号{index}:{school_name}')

        # 让老师选择学校
        choice = input('请输入选择的学校编号:')

        if not choice.isdigit():
            print('请输入正确编号！')
            continue

        choice = int(choice)

        if choice > len(school_li) - 1:
            print('请输入正确编号!')
            continue

        choice_school = school_li[choice]

        # 打印选择的学校下面的课程列表
        flag,course_li_or_msg = common_interface.get_all_course_interface(
            choice_school
        )
        if not flag:
            print(course_li_or_msg)
            continue

        for index1,course_name1 in enumerate(course_li_or_msg):
            print(f'编号{index1}:{course_name1}')

        # 让老师选择课程
        choice1 = input('请输入选择的课程编号:')

        if not choice1.isdigit():
            print('请输入正确编号！')
            continue

        choice1 = int(choice1)

        if choice1 > len(course_li_or_msg) - 1:
            print('请输入正确编号!')
            continue

        choice_course = course_li_or_msg[choice1]

        # 将课程添加到老师的教授列表中
        flag1,msg1 = teacher_interface.choice_teach_course_interface(
            choice_course,teacher_user
        )
        if flag1:
            print(msg1)
            break
        else:
            print(msg1)
            continue


@common.auth('teacher')
def check_course_student():
    while True:
        # 打印学校列表
        flag, school_li = common_interface.get_all_school_interface()
        if not flag:
            print(school_li)
            break

        for index, school_name in enumerate(school_li):
            print(f'编号{index}:{school_name}')

        # 让老师选择学校
        choice = input('请输入选择的学校编号:')

        if not choice.isdigit():
            print('请输入正确编号！')
            continue
        choice = int(choice)

        if choice > len(school_li) - 1:
            print('请输入正确编号!')
            continue
        choice_school = school_li[choice]

        # 打印选择的学校下面的课程列表
        flag, course_li_or_msg = common_interface.get_all_course_interface(
            choice_school
        )
        if not flag:
            print(course_li_or_msg)
            continue

        for index1, course_name1 in enumerate(course_li_or_msg):
            print(f'编号{index1}:{course_name1}')

        # 让老师选择课程
        choice1 = input('请输入选择的课程编号:')

        if not choice1.isdigit():
            print('请输入正确编号！')
            continue
        choice1 = int(choice1)

        if choice1 > len(course_li_or_msg) - 1:
            print('请输入正确编号!')
            continue
        choice_course = course_li_or_msg[choice1] # 这是课程的名字

        # 打印该课程的学生列表
        flag2,msg2 = teacher_interface.show_course_student(
            choice_course
        )
        if flag2:
            for index,student_name in enumerate(msg2):
                print(f'编号{index}:{student_name}')
            break
        else:
            print(msg2)
            continue


@common.auth('teacher')
def change_score():
    while True:
        # 打印学校列表
        flag, school_li = common_interface.get_all_school_interface()
        if not flag:
            print(school_li)
            break

        for index, school_name in enumerate(school_li):
            print(f'编号{index}:{school_name}')

        # 让老师选择学校
        choice = input('请输入选择的学校编号:')

        if not choice.isdigit():
            print('请输入正确编号！')
            continue
        choice = int(choice)

        if choice > len(school_li) - 1:
            print('请输入正确编号!')
            continue
        choice_school = school_li[choice]

        # 打印选择的学校下面的课程列表
        flag, course_li_or_msg = common_interface.get_all_course_interface(
            choice_school
        )
        if not flag:
            print(course_li_or_msg)
            continue

        for index1, course_name1 in enumerate(course_li_or_msg):
            print(f'编号{index1}:{course_name1}')

        # 让老师选择课程
        choice1 = input('请输入选择的课程编号:')

        if not choice1.isdigit():
            print('请输入正确编号！')
            continue
        choice1 = int(choice1)

        if choice1 > len(course_li_or_msg) - 1:
            print('请输入正确编号!')
            continue
        choice_course = course_li_or_msg[choice1]  # 这是课程的名字

        # 打印该课程的学生列表
        flag2, msg2 = teacher_interface.show_course_student(
            choice_course
        )
        if flag2:
            for index, student_name in enumerate(msg2):
                print(f'编号{index}:{student_name}')

        else:
            print(msg2)
            continue

        # 让老师选择学生以及分数
        choice2 = input('请输入选择的学生编号:')

        if not choice2.isdigit():
            print('请输入正确编号！')
            continue

        choice2 = int(choice2)

        if choice2 > len(msg2) - 1:
            print('请输入正确编号!')
            continue

        choice_student = msg2[choice2]  # 这是学生的名字


        while True:
            score = input('请输入该学生分数:')
            if not score.isdigit():
                print('请输入正确的分数！')
                continue
            if not 0 < int(score) < 100:
                print('请输入正确的分数！')
                continue
            break

        # 调用接口进行学生分数修改

        msg3 = teacher_interface.change_score_interface(
            teacher_user,choice_student,score,choice_course
        )
        print(msg3)
        break

function_dic = {
    '1':login,
    '2':check_teach_course,
    '3':choice_teach_course,
    '4':check_course_student,
    '5':change_score,
}


def teacher_view():
    while True:
        print('''
        ========welcome to teacher function========
        1.登录
        2.查看教授课程
        3.选择教授课程
        4.查看课程下学生
        5.修改学生分数
        ====================end====================
        ''')

        choice = input('请输入要进行的操作编号:')

        if choice not in function_dic:
            print('请输入正确编号:')
            continue

        function_dic.get(choice)()
