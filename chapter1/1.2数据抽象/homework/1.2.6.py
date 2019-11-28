"""
如果字符串s中的字符循环移动任意位置之后得到另一个字符串t，那么s就称为t的回环变位。编写一个程序检查两个给定的字符串s和t是否互为回环变位
"""

####思路一：
"""
利用循环的方式遍历字符串t,从循环次数i处将字符串t分成两个字串后交换顺序拼接成一个新的字符串，比较新的s和新的字符串是否相等
"""
def check_circular_rotation1(s, t):
    if len(s) != len(t):
        return False
    for i in range(1, len(t)):
        new_string = t[i:] + t[:i]
        if new_string == s:
            return True
    return False

####思路二：
"""
一行代码，利用index属性
t与t相加，其中必包含s，此时只需查找s的位置即可，绝妙
"""
def check_circular_rotation2(s, t):
    return (len(s) == len(t)) and ((t + t).index(s) > 0)



if __name__ == "__main__":
    a = "ACTGACG"
    b = "TGACGAC"
    print(check_circular_rotation2(a, b))