#!/usr/bin/env python3

from tracer_client import TracerClient

def main():
    c = TracerClient()
    print(c.get(), end='')
    #print(c.get(), end='')

if __name__ == '__main__':
    main()
