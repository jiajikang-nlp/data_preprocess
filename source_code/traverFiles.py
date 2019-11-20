"""
 author:jjk
 datetime:2019/11/20
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 遍历目录文件，打印出所有文件的完整路径
"""
import os,time
"""
遍历目录处理子文件
"""

class TraversalFun():
    # 1、初始化，rootDir目标文件路径
    def __init__(self,rootDir):
        self.rootDir = rootDir

    # 2、遍历目录文件—调用具体的遍历文件名函数
    def TraversalDir(self):
        TraversalFun.AllFiles(self,self.rootDir)

    # 3、递归算法遍历所有文件，并打印文件名(非目录文件)—具体的遍历文件名
    def AllFiles(self,rootDir):
        # 获取根目录下所有文件
        for lists in os.listdir(rootDir):
            path = os.path.join(rootDir,lists) #路径拼接
            if os.path.isfile(path): # 如果是文件
                print('原始文件绝对路径：',os.path.abspath(path)) # 打印绝对路径
            elif os.path.isdir(path): # 如果是一个文件夹
                TraversalFun.AllFiles(self,path) # 递归

if __name__=='__main__':
    time1_start= time.time() # 起始时间

    rootDir = r"../dataSet/Corpus/EnPapers" # 根目录：有很多子目录
    tra = TraversalFun(rootDir) # 调用类函数
    tra.TraversalDir() # 调用一下遍历的方法

    time2_end = time.time() # 结束时间
    print('totall cost:',(time2_end-time1_start),'s') # 微秒









