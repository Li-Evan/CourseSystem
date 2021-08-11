
# 多角色认证装饰器

def auth(role):

    from core import admin_view,student_view,teacher_view
    def deco(func):
        def wrapper(*args,**kwargs):

            if role == 'admin':
                if admin_view.admin_user == None:
                    admin_view.login()
                else:
                    res = func(*args,**kwargs)
                    return res

            if role == 'student':
                if student_view.student_user == None:
                    student_view.login()
                else:
                    res = func(*args,**kwargs)
                    return res


            if role == 'teacher':
                if teacher_view.teacher_user == None:
                    teacher_view.login()
                else:
                    res = func(*args,**kwargs)
                    return res


        return wrapper
    return deco