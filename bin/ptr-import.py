#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Tool to import and index PTR records
#
# Software is free software released under the "Modified BSD license"
#
# Copyright (c) 2013-2014 Alexandre Dulaunoy - a@foo.be

import redis
import argparse

argParser = argparse.ArgumentParser(description='ptr-db: Import and Index PTR records')
argParser.add_argument('-r', action='append', help='Input file in IP,PTR format')
argParser.add_argument('-v', action='store_true', default=False, help='Output inserted PTR records')
args = argParser.parse_args()

def terms(host=None):
    if host is None:
        return False
    p = host.split('.')
    return p

# LevelDB backend using Redis protocol https://github.com/KDr2/redis-leveldb
r = redis.StrictRedis(host='localhost', port=8323)

if args.r:
    for x in args.r:
        with open(x, encoding='UTF-8', errors='ignore') as f:
                for l in f:
                    (ip, ptr) = l.rstrip().split(',')[:2]
                    if args.v:
                        print (terms(ptr))
                    r.set(ip,ptr)
else:
    argParser.print_help()
    exit(1)
