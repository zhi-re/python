#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 大文件切割

import uuid

def writetxt(list,head) :
    uuid_str = uuid.uuid4().hex
    print ("uuid:" ,uuid_str)
    filename = "/tools/" + uuid_str + ".sql"
    foo = open(filename, "w")
    foo.writelines([head])
    foo.writelines(list)
    foo.close

fo = open("/users/script.sql", "r")
list = []
head = fo.readline()
print head
for line in fo :
    list.append(line)
    if len(list)==1000000:
        writetxt(list,head)
        list = []
if len(list) != 0 :
    writetxt(list,head)

fo.close





