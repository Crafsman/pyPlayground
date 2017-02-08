#http://www.runoob.com/python/os-file-methods.html
print('当前文件是： %s' % str(__file__) )

#os.chdir()改变当前工作目录到指定的路径

import os, sys


#查看当前工作目录
current_work_dir = os.getcwd()
print( "当前工作目录是：%s" % (current_work_dir))

#修改当前的工作目录 ch -- change
#os.chdir(path)

abspath = os.path.abspath(__file__)
print( "绝对路径：%s" % abspath)

whatis = os.path.join(os.path.abspath(__file__), os.pardir)
print( "这是什么：%s" % whatis)