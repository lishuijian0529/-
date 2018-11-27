# -*- coding:utf-8 -*-
import socket
import os
import time,threading
import subprocess
from CoordinateData import coordinate
import json
with open('坐标库.txt'.decode('utf-8'), 'r') as f:
    a = json.loads(f.read())
print coordinate().randint(a["Push"]["x"]['value'], a["Push"]["x"]['change'])