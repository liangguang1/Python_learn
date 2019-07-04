# -*- encoding: utf-8 -*-

############### 读取文件 一
'''
try:
   f = open('1111.sql', 'r')
   print(f.read())
finally:
   if f:
      f.close()

############### 读取文件 二
with open('1111.sql','r') as f:
   # print(f.read())
   # print(f.readlines())
   for readline in f.readlines():
      print(readline.strip())
'''

############### 写入数据 （同上一二）
with open('1111.sql', 'w') as f:          ## 将 w 换为 a (append) 表示在文件尾追加。
   f.write('Hellow World!')
   f.close()
with open('1111.sql', 'r') as f:
   print(f.readlines())
   f.close()



##for test