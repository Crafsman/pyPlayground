#http://www.runoob.com/python/os-file-methods.html
print('当前文件是： %s' % __file__ )

#os.chdir()改变当前工作目录到指定的路径

import os, sys
path = "temp"

#查看当前工作目录
current_work_dir = os.getcwd()
print( "当前工作目录是：%s" % str(current_work_dir))

#修改当前的工作目录 ch -- change
os.chdir(path)

current_work_dir = os.getcwd()
print( "当前工作目录是：%s" % str(current_work_dir))