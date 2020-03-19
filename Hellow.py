# -*- coding: utf-8 -*-
# @Author  : wei mengbao
# @Email   : u8tou@qq.com
# @project : robot
# @Time    : 2020/2/24 13:29

def robot():
    print('''
             __
     _(\    |@@|
    (__/\__ \--/ __
       \___|----|  |   __
           \ }{ /\ )_ / _\
           /\__/\ \__O (__
          (--/\--)    \__/
          _)(  )(_
         `---''---`
         ''')

def hellow(username,robor_name):
    print('你好呀！,'+username+',我是'+robor_name+',很高兴为您服务！这是第一种打招呼的方式')

    print('你好呀！,{},我是{},很高兴为您服务！这是进阶版的打招呼方式'.format(username,robor_name))

    print(f'你好呀！,{username},我是{robor_name},很高兴为您服务！这是最终版的打招呼方式')

    print(1,2,3,4,5,6,7)

    print(f'I\'m {robor_name}!')
def ask():
    userName = input('你好呀~我叫U8机器人，你的名字是？\n')
    age = input('很高兴能为你服务，你今年多少年纪了呢？\n')
    age = int(age)
    if(age < 12):
        print(f"{age}岁？跟我一样的小P孩")
    elif(age <= 30):
        print(f"{age}岁？充满无限可能的年纪！！！")
    elif(age < 50):
        print(f"{age}岁？沉稳的年纪！！！")
    else:
        print(f'{age},丰富的人生阅历！！！')
    return userName
