#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在用户管理功能中添加密码信息:
#	增、改添加用户密码输入                 ##  这里修改题义为(添加add/修改update/删除delete时，增加密码输入认证信息)
#	显示时将用户密码显示为N(密码长度)个*   ##  输入密码时将用户密码显示为N个*，不能显示出密码字符
#	用户验证修改为用户名和密码
#
#	输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序）后将结果输入



import sys, tty, termios

#for python 3.x

def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

def getpass(maskchar = "*"):
  password = ""
  while True:
    ch = getch()
    if ch == "\r" or ch == "\n":
      print
      return password
    elif ch == "\b" or ord(ch) == 127:
      if len(password) > 0:
        sys.stdout.write("\b \b")
        password = password[:-1]
    else:
      if maskchar != None:
        sys.stdout.write(maskchar)
      password += ch


def pt():                                      ## 打印函数
    print("用户名:{}".format(i, ))
    print("年龄:{}".format(k[0]))
    print("联系方式:{}".format(k[1]))
    print("密码:{}".format(len(k[2])*'*'))
    print("-----------------------")



info = {"candy": [10,13912099188,'redhat'], "litchi": [30,13512500991,'centos'], "beattie": [32,13820999133,'ubuntu']}   ## list中最后list[-1]为密码信息
user = []
for key in info.keys():
    user.append(key)



while True:
    input_str = input("请从列表中选择操作字符[add,delete,update,find,list,exit(退出程序)]:")

    if input_str == "delete":
        input_user = input("请输入删除用户昵称:")

        if input_user in user:
            print("Enter your password:") 
            input_password = getpass("*")
            print(' ')
        
            if input_password == info[input_user][2] :
                info.pop(input_user)
                user.remove(input_user)
                print("该用户删除成功！")
            else:
                print("验证失败，未能删除该用户！")

        else:
            print("此用户不存在!")


    elif input_str == "add":
        input_user = input("请输入任意用户,认证通过后可添加新用户:")

        if input_user in user:
            print("Enter your password:")
            input_password = getpass("*")
            print(' ')

            if input_password == info[input_user][2] :
                input_add = input("请按照(用户名:年龄:联系方式:密码)格式输入:")  ## jerry:10:13821099101:busybox

                if input_add.split(":")[0] not in user :
                    info[input_add.split(":")[0]] = [int(input_add.split(":")[1]), int(input_add.split(":")[2]),(input_add.split(":")[3])]
                    user.append(input_add.split(":")[0])
                    print("用户添加成功!")

                else:
                    print("不能修改该用户,该用户已存在!")  

            else:
                print("验证失败,无法添加新用户!")
        else:
            print("无此用户!")



    elif input_str == "update":
        input_user = input("请输入更改用户昵称:")

       # if input_user in user:
       #     input_password = input("验证该用户密码:")

        if input_user in user:
            print("Enter your password:") 
            input_password = getpass("*")
            print(' ')

            if input_password == info[input_user][2]:
                input_full = input("请按照(用户名:年龄:联系方式:密码)格式输入:")  ## candy:10:13821099101:busybox

                if input_full.split(":")[0] == input_user:
                    info[input_full.split(":")[0]] = [int(input_full.split(":")[1]), int(input_full.split(":")[2]),str(input_full.split(":")[3])]
                    print("该用户信息修改成功！")
                else:
                    print("提示：操作不成功，请检查输入格式，且只能修改{}信息，无法修改其它用户信息!".format(input_user,))

            else:
                print("验证失败，不能修改该用户信息！")



    elif input_str == "find":
        input_find = input("请输入查找用户名:")

        if input_find in user:
            print('年龄 {},联系方式:{}'.format(info[input_find][0],info[input_find][1]) )
        else:
            print("此用户不存在!")



    elif input_str == "list":
        name_lst = []
        age_lst = []
        tel_lst = []

        for i,k in info.items():
            name_lst.append(i)
            age_lst.append(k[0])
            tel_lst.append(k[1])

        age_order = sorted(age_lst,reverse=False)
        tel_order = sorted(tel_lst,reverse=False)
        name_order = sorted(name_lst,reverse=False)

        # print(name_lst)
        # print(age_lst)
        # print(tel_lst)

        input_order = input("请从{name,age,tel}中选择输入一个字段排序并打印，输入任意键默认以name排序：")

        if input_order == 'age':
            for j in age_order:
                for i, k in info.items():
                    if k[0] == j:
                        pt()

        elif input_order == 'tel':
            for j in tel_order:
                for i, k in info.items():
                    if k[1] == j:
                        pt()

        elif input_order == 'name':
            for j in name_order:
                for i, k in info.items():
                    if i == j:
                        pt()

        else:
            for j in name_order:
                for i, k in info.items():
                    if i == j:
                        pt()


    

    elif input_str == "exit":
        break



    else:
        print("输入不合法，请重新输入！")

print(info)

