"""
 author:jjk
 datetime:2019/11/22
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 实现普通的斐波那锲数列和yield实现斐波那锲数列
 
"""
import time
"""
斐波那锲数列：1,1,2,3,5，8,13,21,34,55,89,144...
        从数列的第三项开始，后面每一项是前面两项之和
数学描述：F(0)=1,F(1)=1,...F(n)=F(n-1)+F(n-2) (n>=2，n∈N*)
"""

# 普通的斐波那锲数列
def fab1(max):
    n,a,b = 0,0,1 # a=0,b=1
    while n<max:
        if n<20: print('->',b)
        # print('->',b)
        a,b = b,a+b
        n = n+1 # n表示最大的第几项

# 斐波那锲数列算法生成器实
def fab2(max):
    n,a,b = 0,0,1
    while n<max:
        yield b # #yield是一个关键词，类似return, 不同之处在于，yield返回的是一个生成器
        # return b
        a,b = b,a+b
        n = n + 1

def GeneratorDome():
    maxnum = 500000 # 最大迭代数
    # 普通算法实现斐波那锲数列
    t1 = time.time()
    fab1(maxnum)
    t2 = time.time()
    print('Fab1 Total Time %.f：' % ((t2-t1)) + 's') # 输出耗费时间

    # yield生成器实现斐波那锲数列
    t3 = time.time()
    b = fab2(maxnum)
    t4 = time.time()
    print('Fab2 Total Time %.f：' % ((t4 - t3)) + 's')  # 输出耗费时间

if __name__ == '__main__':
    GeneratorDome() # 实例化
