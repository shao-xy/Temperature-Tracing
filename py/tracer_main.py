#!/usr/bin/env python3

import sys
import os
from tracer import Tracer

def check_uid():
    if os.getuid() != 0:
        sys.stdout.write('Must be root to execute.\n')
        sys.exit(-1)

def record_pid():
    with open('/var/run/temperature_pid', 'w') as fout:
        fout.write(str(os.getpid()))

def main():
    check_uid()
    record_pid()
    Tracer().launch()

if __name__ == '__main__':
    sys.exit(main())
