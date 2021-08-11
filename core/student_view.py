from interface import student_interface
from lib import common,common_interface

student_user =None

def regester():
    while True:
        student_name = input('请输入用户名:')
        student_password = input('请输入密码:')

        flag,msg = student_interface.regester_interface(
            student_name,student_password
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue

def login():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码:')

        flag,msg = common_interface.login_interface(
            username,password,user_type='student'
        )

        if flag:
            print(msg)
            global student_user
            student_user = username
            break
        else:
            print(msg)
            continue

@common.auth('student')
def choice_school():

    # 打印所有学校
    flag,school_li = common_interface.get_all_school_interface()
    for index,school_name in enumerate(school_li):
        print(f'编号{index}:{school_name}')

    # 接收输入的选择的学校
    choice_school_name = None
    while True:
        choice = input('请输入需要选择的学校的编号:')

        if not choice.isdigit():
            print('请输入正确编号!')
            continue
        choice = int(choice)

        if choice > len(school_li)-1:
            print('请输入正确编号！')
            continue

        choice_school_name = school_li[choice]
        break
    # 调用接口进行学校选择的逻辑判断
    msg = student_interface.choice_school_interface(
        choice_school_name,student_user
    )

    print(msg)

@common.auth('student')
def choice_course():
    while True:
        # 打印学生所选择的学校下属课程列表
        flag,msg_or_li = student_interface.get_all_course_interface(
            student_user
        )
        if not flag:
            print(msg_or_li)
            return
        if flag:
            for index,course in enumerate(msg_or_li):
                print(f'编号{index}:{course}')

        # 学生选择课程
        choice_course_name = None
        choice = input('请输入选择的课程编号:')


        if not choice.isdigit():
            print('请输入正确编号!')
            continue

        choice = int(choice)

        if choice > len(msg_or_li)-1:
            print('请输入正确编号！')
            continue

        choice_course_name = msg_or_li[choice]

        # 调用接口进行保存
        flag2,msg = student_interface.choice_course_interface(
            choice_course_name,student_user
        )
        if flag2:
            print(msg)
            break
        else:
            print(msg)
            continue




@common.auth('student')
def check_score():
    flag,msg_or_score_dic = student_interface.check_score_interface(
        student_user
    )


    print(msg_or_score_dic)


function_dic = {
    '1':regester,
    '2':login,
    '3':choice_school,
    '4':choice_course,
    '5':check_score,
}
def student_view():
    while True:
        print('''
        ===========welcome to student function============
        1.注册
        2.登录功能
        3.选择校区
        4.选择课程
        5.查看分数
        =======================end========================
        ''')

        choice = input('请输入要进行的操作编号:')

        if not choice in function_dic:
            print('请输入正确编号')
            continue

        function_dic.get(choice)()