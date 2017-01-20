import re
import sys
import urllib.request
# f_copystr = []
#
# file_str = 'where is file?\n i am here'
# f = open('whereis.txt', 'w')
# f.writelines(file_str)
# f.close()
# old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
# total_page = 20
#
# f = open('text.txt', 'r')
# html = f.read()
# f.close()

# for i in range(0, 10):
#     print(i)
# for i in sys.path:
#     print(i)
#
# sys.exit('finish')

#Read source.txt file
# f = open('source.txt', 'r')
# html = f.read()
# f.close()

print(re.search(r'\d', 'I love 124 FishC.com'))

#匹配IP地址的
#re.search(r'[01]\d\d|2[0-4]|25[0-5]','188')
#re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]|25[0-5])\.){3}([01]{0,1}\d\{0,1}d|2[0-4]|25[0-5])','192.168.1.1')
