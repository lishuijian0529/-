# -*- coding:utf-8 -*-
import random
import time
import json
import string
class coordinate():
    def  randint(self,x,i):
        return random.randint(x-i,x+i)


if __name__ == '__main__':
    #with open('坐标库.txt'.decode('utf-8'),'r') as f:
    #    a= json.loads(f.read())
    #print coordinate().randint(a["Push"]["x"]['value'],a["Push"]["x"]['change'])
    #print coordinate().randint(a["a"]["x"]['value'],a["a"]["x"]['change'])
    #u='13161759881'
    #for i in list(u):
    #    print coordinate().randint(a['%s'%i]["x"]['value'], a['%s'%i]["x"]['change'])
    #    print coordinate().randint(a['%s' % i]["y"]['value'], a['%s' % i]["y"]['change'])
    keylist = ''.join([random.choice(string.ascii_lowercase) for i in range(8)])
    print keylist