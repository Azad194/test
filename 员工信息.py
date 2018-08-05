# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 12:55:41 2018

@author: Azad
"""
#查询修改用户信息



def user_info_get():
    path = input('请输入文件路径')
    global file
    file = open(path,"r+",encoding = "utf-8")
    raw_date = file.readlines()
    account_dic = {}
    for line in raw_date:
        line_str = line[0:-1]
        line_list = line_str.split(",")
        account_dic[line_list[0]] = line_list
    return(account_dic)
    
    
def user_info_save(dic):
    file.seek(0)
    file.truncate()
    for account_list in dic.values():
        account_str = ','.join(account_list)
        file.write("%s\n"% account_str)
    file.flush()
#    print(dic.values())
    
def main():
    print('''
      1.修改个人信息
      2.打印个人信息
      3.修改密码
      4.返回主页
          ''')
    chioce = input('>>>')
    return(chioce)


def user_info_change():
    chioce2 = eval(input('''
       ------------------
        1  Name:   %s  
        2  Age :   %s  
        3  Job :   %s  
        4  Dept:   %s  
        5  Phone:  %s  
       ------------------
       请输入预想修改内容的编号
        '''%(accounts[username][2],
             accounts[username][3],
             accounts[username][4],
             accounts[username][5],
             accounts[username][6])
                   ))
    if chioce2 in [1,2,3,4,5]:
        accounts[username][chioce2+1] = input("请输入您想修改的信息")
        print("修改完毕")
    else:
        print("请输入正确编号")
#    print(accounts)


def user_info_print():
    print('''
        ------------------
        Name:   %s
        Age :   %s
        Job :   %s
        Dept:   %s
        Phone:  %s
        ------------------
        '''%(accounts[username][2],
             accounts[username][3],
             accounts[username][4],
             accounts[username][5],
             accounts[username][6])
        )


def password_change():
    password = input("请输入原密码")
    if password == accounts[username][1]:
        new_password = input("请输入要修改的密码")
        confirm_password = input("请再次输入密码")
        if new_password == confirm_password:
            accounts[username][1] = new_password
            print("密码修改成功")
        else:
            print("请确认两次输入的密码是否有误")
    else:
        print("密码输入错误")



accounts = user_info_get()
a = 0
while a < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username in accounts:
        if password == accounts[username][1]:
            print("welcome %s".center(50,'-') % username)
            while True:    
                chioce = int(main())
                if chioce == 1:
                    user_info_change()
                    user_info_save(accounts)
                elif chioce == 2:
                    user_info_print()
                elif chioce == 3:
                    password_change()
                    user_info_save(accounts)
                elif chioce == 4:
                    break
                else:
                    print("place input the right number,")
            break
        else:
            print ("Worng password!")
    else:
        print("Username does not exist.")
    a += 1
else:
    print("Too many attempts.")
            
file.close()







