"""
 author:jjk
 datetime:2019/11/19
 coding:utf-8
 project name:Pycharm_workstation
 Program function: 多格式的文本信息抽取工具
"""

import fnmatch,os
from win32com import client as wc
from win32com.client import Dispatch

"""
功能描述：抽取多文档文本，默认保存在根目录下，支持自定义
参数描述：1、filePath：文件路径；2、savePath：保存路径
"""

def Files2Txt(filePath,savePath=''):
    try:
        # 1、切分文件上级目录和文件名路径
        dirs, filename = os.path.split(filePath)
        print('原文件路径：', dirs)
        print('原文件名：', filename)

        # 2、修改切分后的文件名后缀
        typename = os.path.splitext(filename)[-1].lower()  # 切分文件名获取后缀
        print('typename=', typename)
        new_name = TranType(filename, typename)  # 文件名，文件类型名
        print('新的文件名：',new_name)

        # 3、文件转化后的保存路径
        if savePath == '':
            savePath = dirs
        else:
            savePath = savePath
        new_save_path = os.path.join(savePath, new_name)
        print('保存路径：', new_save_path)

        # 4、加载文本提取的处理程序
        wordapp = wc.Dispatch('Word.Application')  # 启动应用程序
        mytxt = wordapp.Documents.Open(filePath)  # 打开文件路径
        # 5、保存文本信息
        mytxt.SaveAs(new_save_path, 4)
        mytxt.close()
    except Exception as e:
        pass # 这里给出的异常直接跳过

"""
功能描述：根据文件后缀修改文件名
参数描述：1、filePath：文件路径；2、typename：文件后缀
返回数据：new_name 返回修改后的新的文件名
"""
def TranType(filename,typename):
    # 新的文件名称
    new_name = ''
    if typename == '.pdf':# pdf-->txt
        if fnmatch.fnmatch(filename,'*.pdf'):
            new_name = filename[:-4] + '.txt'
        else:return
    elif typename == '.doc' or typename == '.docx': # word-->txt
        if fnmatch.fnmatch(filename,'*.doc'):
            new_name = filename[:-4] + '.txt'
        elif fnmatch.fnmatch(filename,'*.docx'):
            new_name = filename[:-5] + '.txt'
        else:return
    else:
        print('警告：您输入【',typename,'】数据不合法，本抽取工具仅支持doc/docx/pdf格式文件，请输入正确格式')
        return
    return new_name

if __name__ == '__main__':
    filePath1 = os.path.abspath(r'../dataSet/Corpus/wordtotxt/test_word1.doc')
    filePath2 = os.path.abspath(r'../dataSet/Corpus/pdftotxt/一种改进的朴素贝叶斯文本分类方法.pdf')
    filePath3 = os.path.abspath(r'../dataSet/Corpus/wordtotxt/test_word2.docx')
    Files2Txt(filePath3)