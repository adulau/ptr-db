#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Tool to query an IPv4 subnet for existing PTR records
#
# Software is free software released under the "Modified BSD license"
#
# Copyright (c) 2013-2014 Alexandre Dulaunoy - a@foo.be


import redis
import argparse
import netaddr

argParser = argparse.ArgumentParser(description='ptr-db: Search PTR records')
argParser.add_argument('-s', action='append', help='IPv4 subnet to lookup')
argParser.add_argument('-v', action='store_true', default=False, help='Verbose output including non-existing PTR records')
args = argParser.parse_args()

if args.s is None:
    argParser.print_help()
    exit(1)


# LevelDB backend using Redis protocol https://github.com/KDr2/redis-leveldb
r = redis.StrictRedis(host='localhost', port=8323)

for subnet in args.s:
    iplist = netaddr.IPNetwork(subnet)
    for ip in iplist:
        ptr = r.get(ip)
        if ptr is not None:
            print (str(ip)+","+str(r.get(ip), 'utf-8'))
        else:
            if args.v:
                print (str(ip))
