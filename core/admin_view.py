from interface import admin_interface,student_interface,teacher_interface
from lib import common,common_interface

admin_user = None

def register():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        re_password = input('请再次输入密码:')

        if password != re_password:
            print('两次密码不一致，请重新输入!')

        else:
            flag,msg = admin_interface.register_interface(
                username,password
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
            username,password,user_type='admin'
        )

        if flag:
            print(msg)
            global admin_user
            admin_user = username
            break
        else:
            print(msg)
            continue


@common.auth('admin')
def create_school():
    while True:
        school_name = input('请输入学校名称:')
        school_addr = input('请输入学校地址:')

        flag,msg = admin_interface.create_school_interface(
            school_name,school_addr,admin_user
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


@common.auth('admin')
def create_course():
    while True:
        # 打印学校并让用户选择
        flag,msg_or_li = common_interface.get_all_school_interface()

        if not flag:
            print(msg_or_li)

        else:
            for index,name in enumerate(msg_or_li):
                print(f'编号{index}:{name}')

            choice = input('请输入对应学校编号:')

            if not choice.isdigit():
                print('请输入正确编号！')
                continue
            choice = int(choice)

            if choice > len(msg_or_li):
                print('请输入正确编号！')
                continue
            school_name = msg_or_li[choice]

            # 调用接口进行课程创建，并绑定给对应学校
            course_name = input('请输入需要创建的课程名:')
            course_cycle = input('请输入课程周期:')

            flag,msg = admin_interface.create_course_interface(
                admin_user,school_name,course_name,course_cycle
            )
            # 打印信息
            if flag:
                print(msg)
                break
            else:
                print(msg)
                continue



@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入需要创建的老师:')
        flag,msg = admin_interface.create_teacher_interface(
            teacher_name,admin_user
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            continue


function_dic = {
      '1':register,
      '2':login,
      '3':create_school,
      '4':create_course,
      '5':create_teacher,
}



def admin_view():
    while True:
        print(
            '''
            =========welcome to admin_view function========
            1.注册
            2.登录
            3.创建学校
            4.创建课程
            5.创建讲师
            ======================end======================
            '''
        )

        choice = input('请输入要进行的操作:')

        if choice not in function_dic:
            print('请输入正确的编号:')

        else:
            function_dic[choice]()