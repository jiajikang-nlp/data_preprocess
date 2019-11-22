"""
 author:jjk
 datetime:2019/11/20
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 批量抽取

"""

import os,time
import extractTxt as ET

"""
功能描述：遍历目录处理子文件，抽取其文本
参数描述：1 rootDir 根目录，2 func 方法参数，3 saveDir 保存路径
"""

"""
1、引用外部文本抽取模块：import ExtractTxt as ET
2、参数方法使用：TraversalFun(rootDir,ET.File2Txt,saveDir)
3、 创建保存根目录：os.path.abspath
4、递归遍历文件：func(path,save_dir)
"""

class TraversalFun():
    # 1、初始化，rootDir目标文件路径
    def __init__(self,rootDir,func=None,saveDir=""): # saveDir：保存路径，
        self.rootDir = rootDir # 目标文件夹路径
        self.func = func # 方法参数，实现文本提取
        self.saveDir = saveDir # 文件夹保存路径，

    # 2、遍历目录文件—调用具体的遍历文件名函数
    def TraversalDir(self):
        # 分切文件目录和文件名
        dirs,filename = os.path.split(self.rootDir)
        print('dirs:',dirs) # 根路径
        print('filename=',filename) # 文件夹名称

        # 保存目录
        save_dir = ""
        if self.saveDir == "":
            save_dir = os.path.abspath(os.path.join(dirs,'new_'+filename)) # 文件夹保存的路径
        else:save_dir = self.saveDir
        print('save_dir=',save_dir) # 打印最新的文件夹所在路径

        # 创建保存路径-创建目录文件
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)  # 创建文件路径
        print("保存目录：",save_dir)
        # 遍历文件并将其转化txt文件
        TraversalFun.AllFiles(self, self.rootDir,save_dir) # 根路径和保存路径

    # 3、递归算法遍历所有文件，并打印文件名(非目录文件)—具体的遍历文件名（递归遍历所有文件，并提供具体文件操作功能）
    def AllFiles(self,rootDir,save_dir=''):
        # 返回指定目录包含的文件或文件夹的名字的列表
        # 获取根目录下所有文件
        for lists in os.listdir(rootDir):
            # 待处理文件夹名称集合
            path = os.path.join(rootDir,lists)  # 路径拼接
            # 核心算法：对文件类型信息抽取，并保存
            if os.path.isfile(path):  # 如果是文件
                self.func(os.path.abspath(path),os.path.abspath(save_dir)) # 文件名和保存路径
                print('原始文件绝对路径：', os.path.abspath(path))  # 打印绝对路径

            # 递归遍历文件目录
            if os.path.isdir(path):  # 如果是一个文件夹
                newpath = os.path.join(save_dir,lists) # save_dir+列表
                if not os.path.exists(newpath): # 如果不存在这样的路径
                    os.mkdir(newpath) # 创建
                TraversalFun.AllFiles(self, path,newpath)  # 递归调用函数


if __name__=='__main__':
    time_start = time.time() # 起始时间

    # 根目录文件路径
    rootDir = os.path.abspath(r'../dataSet/Corpus/EnPapers')
    # 自定义保存路径
    #saveDir = r'../Corpus'
    #tra = TraversalFun(rootDir,ET.Files2Txt,saveDir)
    # 默认方法参数打印所有文件路径
    tra = TraversalFun(rootDir,ET.Files2Txt) # 参数二：文本抽取的方法，保存路径可以为空，
    tra.TraversalDir() # 调用一下参数的方法

    time_end = time.time() # 终止时间
    print('Totall cost:',(time_end-time_start)*1000,'ms')