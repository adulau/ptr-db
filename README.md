ptr-db - PTR DNS records database
=================================

A ptr-db is a database to store, index and lookup large set of PTR DNS records.

Requirements
------------

- Python 3
- Python [redis](https://pypi.python.org/pypi/redis/) client
- Redis [LevelDB server](https://github.com/KDr2/redis-leveldb)
- [netaddr](https://github.com/drkjam/netaddr)

Usage
-----

```shell
./bin/ptr-search.py -s 108.4.0.0/28
108.4.0.1,L100.RCMDVA-VFTTP-20.verizon-gni.net
108.4.0.2,pool-108-4-0-2.rcmdva.fios.verizon.net
108.4.0.3,pool-108-4-0-3.rcmdva.fios.verizon.net
108.4.0.4,pool-108-4-0-4.rcmdva.fios.verizon.net
108.4.0.5,pool-108-4-0-5.rcmdva.fios.verizon.net
108.4.0.6,pool-108-4-0-6.rcmdva.fios.verizon.net
108.4.0.7,pool-108-4-0-7.rcmdva.fios.verizon.net
108.4.0.8,pool-108-4-0-8.rcmdva.fios.verizon.net
108.4.0.9,pool-108-4-0-9.rcmdva.fios.verizon.net
108.4.0.10,pool-108-4-0-10.rcmdva.fios.verizon.net
108.4.0.11,pool-108-4-0-11.rcmdva.fios.verizon.net
108.4.0.12,pool-108-4-0-12.rcmdva.fios.verizon.net
108.4.0.13,pool-108-4-0-13.rcmdva.fios.verizon.net
108.4.0.14,pool-108-4-0-14.rcmdva.fios.verizon.net
108.4.0.15,pool-108-4-0-15.rcmdva.fios.verizon.net
```
