"""
 author:jjk
 datetime:2019/11/22
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 递归批量到处去30w新闻文本
 
"""

import os,time

"""
功能描述：遍历目录，对子文件单独处理

"""

# 遍历目录文件
def TraversalDir(rootDir):
    # 返回指定目录包含的文件或文件夹的名字的列表
    for i, lists in enumerate(os.listdir(rootDir)): # 枚举的方式（listdir返回指定的文件夹包含的文件或文件夹的名字的列表）
        # 待处理文件夹名字列表
        path = os.path.join(rootDir,lists) #拼接
        # 核心算法，对文件具体操作
        if os.path.isfile(path):# 如果这个路径是一个文件
            if i%10000 == 0:
                print('{t} *** {i} \t docs has been read'.format(i=i,t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
        # 递归遍历文件目录
        if os.path.isdir(path):# 如果是一个目录
            TraversalDir(path)


if __name__ == '__main__':
    t1 = time.time()
    rootDir = r'../dataSet/CSCMNews' # 读取路径
    TraversalDir(rootDir)
    t2 = time.time() # 运行时间
    print('Total Cost Time %.2f' %(t2-t1)+ 's')