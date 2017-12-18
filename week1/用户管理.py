#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用户管理
#
#如果输入delete，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
#
#如果输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找dcit中数据，若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在;
#
#如果用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据包含输入字符串的用户信息，并打印;
#
#如果用户输入list，则打印所有用户信息;
#
#打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
#
#如果用户输入exit，则打印退出程序，并退出 ;


info = {"candy": [10, 13512099188], "litchi": [30, 13512500991], "beattie": [32, 13920999133]}
user = []
for key in info.keys():
    user.append(key)

while True:
    input_str = input("请从列表中选择操作字符[delete,update,find,list,exit(退出程序)]:")

    if input_str == "delete":
        input_user = input("请输入用户名称:")

        if input_user in user:
            info.pop(input_user)
            user.remove(input_user)

        else:
            print("此用户不存在!")

    elif input_str == "update":
        input_full = input("请按照(用户名:年龄:联系方式)格式输入:") ## candy:10:13821099101

        if input_full.split(":")[0] in user:
            info[input_full.split(":")[0]] = [int(input_full.split(":")[1]),int(input_full.split(":")[2])]
        else:
            print("此用户不存在!")

    elif input_str == "find":
        input_find = input("请输入查找用户名:")

        if input_find in user:
            print(info[input_find])
        else:
            print("此用户不存在!")

    elif input_str == "list":
        #print(info)
        for i,k in info.items():
            print("用户名:{}".format(i,))
            print("年龄:{}".format(k[0]))
            print("联系方式:{}".format(k[1]))
            print("*************************")

    elif input_str == "exit":
        break

    else:
        print("输入不合法，请重新输入！")

# print(user)
print(info)
