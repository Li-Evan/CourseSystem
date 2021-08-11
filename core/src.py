from core import admin_view
from core import teacher_view
from core import student_view


function_dic = {
    '1':admin_view.admin_view,
    '2':teacher_view.teacher_view,
    '3':student_view.student_view,
}

def run():
    while True:
        print(
            '''
            ========welcome to coursesystem=======
            1.管理员功能
            2.教师功能
            3.学生功能
            ==================end=================
            '''
        )

        choice = input('请输入要登录的用户类别:')

        if choice not in function_dic:
            print('请输入正确的编号:')

        else:
            function_dic[choice]()