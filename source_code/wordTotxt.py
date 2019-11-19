"""
 author:jjk
 datetime:2019/11/4
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 抽取word文档文本内容转换成txt格式

"""

"""
功能描述：word文件转存txt，默认保存在根目录下，支持自定义
参数描述：1、filePath：文件路径；2、savePath：保存路径
"""
"""
实现步骤：
    # 1、切分文件路径为文件目录和文件名
    # 2、修改切分后的文件后缀
    # 3、设置新的文件保存路径
    # 4、加载文本提取的处理程序，word->txt
    # 5、保存文本信息
"""
import os # 路径
import fnmatch # 后缀名的一个包
from win32com import client as wc
from win32com.client import Dispatch,DispatchEx

def Word2Txt(filePath,savePath=''):
    # 1、切分文件路径为文件目录和文件名
    dirs,filename = os.path.split(filePath)
    print('原始路径：',dirs)
    print('原始文件名：',filename)
    # 2、修改切分后的文件后缀
    new_name = "" #设置一个新的文件名
    if fnmatch.fnmatch(filename,'*.doc'): # 如果文件名后缀是以docx结尾的，则
        new_name = filename[:-4] + '.txt' # 截取直到倒数后四位，保留除后四位其余的内容
    elif fnmatch.fnmatch(filename,'*.docx'):
        new_name = filename[:-5] + '.txt'  # 截取直到倒数后5位，保留除后五位其余的内容
    else:
        print('格式不正确，仅支持doc or docx 格式')
        return
    # 3、设置新的文件保存路径
    if savePath == '':
        savePath = dirs # 保存到原始路径
    else:
        savePath = savePath # 传递的路径
    word2txtPath = os.path.join(savePath,new_name) # 连接
    print('最新文件路径及文件名：',word2txtPath)

    # 4、加载文本提取的处理程序，word->txt
    wordapp = wc.Dispatch('Word.Application') # 启动应用程序
    # wordapp.Visible = True
    # wordapp.DisplayAlerts = 0
    mytxt = wordapp.Documents.Open(filePath) # 打开文件路径

    # 5、保存文本信息
    mytxt.SaveAs(word2txtPath,4) # 以txt格式保存，参数4代表抽取文本
    mytxt.Close()
    # wordapp.Quit()


if __name__ == '__main__':
    filePath = os.path.abspath(r'../dataSet/Corpus/wordtotxt/test_word1.docx') # 获取绝对路径
    Word2Txt(filePath)# 函数实例化
    print('word信息抽取到txt格式中完成')









