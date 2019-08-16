import os
import sys

argvs = sys.argv
argc = len(argvs)

if argc != 2:
    print 'Usage: # python %s prototxt'     % argvs[0]
    quit()
prototxt = argvs[1]
f = open(prototxt, 'r')
lines = f.readlines()
f.close()

f = open(prototxt, 'w')
flag = False
for line in lines:
    if(flag == False and "transform_param" in line):
        flag = True
    if(flag == True):
        line = "# " + line
    if(flag == True and "}" in line):
        flag = False
    f.write(line)
f.close()
