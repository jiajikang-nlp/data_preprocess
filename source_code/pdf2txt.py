"""
 author:jjk
 datetime:2019/11/19
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 抽取pdf文件内容转换为txt格式内容
 
"""
import fnmatch,os
from win32com import client as wc
from win32com.client import Dispatch

"""
功能描述：PDF文件转存txt，默认保存在根目录下，支持自定义
参数描述：1、filePath：文件路径；2、savePath：保存路径
"""
"""
实现步骤：
    定义文件路径和转存路径：split
    修改新的文件名：fnmatch
    设置完整的保存路径：join
    启动应用程序格式转换：Dispatch
    保存文本：SaveAs
"""

def Pdf2Txt(filePath,savePath=''):
    # 1、切分文件路径为文件目录和文件名
    dirs,filename = os.path.split(filePath)
    print('原始文件路径：',dirs)
    print('原始文件名：',filename)
    # 2、修改切分后的文件后缀
    new_name = ""
    if fnmatch.fnmatch(filename,'*.pdf') or fnmatch.fnmatch(filename,'*PDF'):
        new_name = filename[:-4] + '.txt' # 更新文件后缀名
    else:
        print('格式不正确，仅支持pdf格式')
        return
    # 3、设置新的文件保存路径
    if savePath=='':
        savePath = dirs
    else:
        savePath =savePath
    pdf2txtPath = os.path.join(savePath,new_name)
    print('新的文件名=',pdf2txtPath)

    # 4、加载文本提取的处理程序，pdf->txt
    wordapp = wc.Dispatch('Word.Application') # 启动应用程序
    mytxt = wordapp.Documents.Open(filePath) # 打开文件路径
    # 5、保存文本信息
    mytxt.SaveAs(pdf2txtPath,4) # 以txt格式保存，参数4代表抽取文本
    mytxt.Close()

if __name__ == '__main__':
    filePath = os.path.abspath(r'../dataSet/Corpus/pdftotxt/一种改进的朴素贝叶斯文本分类方法.pdf')
    Pdf2Txt(filePath)