#!/usr/bin/env python3

import sys
sys.path.insert(0, '/home/sxy/temperature_tracer/py')

import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

import util
from tracer_client import TracerClient

def to_http(s):
    return s.strip().replace('°', '&deg;')

def main():
    print("""Content-type: text/html

<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>403机房主机skv-node5温度</title>
</head>
<body>
<h1>当前温度</h1>
%s
<h1>历史温度</h1>
""" % (to_http(util.instant_temperature_status())))
    c = TracerClient()
    for line in c.get().split('\n'):
        line = to_http(line)
        print(f'{line}<br>')
    print("""
</body>
</html>
""")

if __name__ == '__main__':
    main()

