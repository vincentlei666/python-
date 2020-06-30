# -*- coding:utf-8 -*-

from core import admin
from core import student
from core import teacher

func_dic = {
    '1':admin.admin_view,
    '2':student.student_view,
    '3':teacher.teacher_view
}

def run():
    while True:
        print("""
        ======== 选课系统 ========
                1、管理员功能
                2、学生功能
                3、老师功能
        =========== END ==========
        """)
        choice = input('请输入功能编号(输入q退出):').strip()
        if choice == 'q':
            break
        if choice not in func_dic:
            print('请输入正确的功能编号。')
            continue
        func_dic.get(choice)()










