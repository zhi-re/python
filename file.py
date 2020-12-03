#!/usr/bin/python
# coding=utf-8

# 打开一个文件
fo = open("/tools/test.txt", "a")
print "文件名: ", fo.name

fo.write("3534认为5\n")
# 关闭打开的文件
fo.close()


# 打开一个文件
fo = open("/tools/test.txt", "r+")
str = fo.read(10)
print "读取的字符串是 : ", str

# 查找当前位置
position = fo.tell()
print "当前文件位置 : ", position
 
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print "重新读取字符串 : ", str

for index in range(5):
    line = fo.next()
    print "第 %d 行 - %s" % (index, line)

print index

# 关闭打开的文件
fo.close()

fo = open("/users/test.txt", "r")

i = 0
l = []
for line in fo : 
    #print i
    i +=1
    if '24323' in line :
        l.append(line)
        print line 
print l 
fo.close()
print "ok"

