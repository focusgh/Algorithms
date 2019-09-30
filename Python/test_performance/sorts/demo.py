#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

import random
import time

from Python.sorts.insertion_sort import insertion_sort
from Python.sorts.bubble_sort import bubble_sort


class Demo(object):

    def __init__(self):
        pass

    def run(self):
        # 13.457926034927368 s
        # 14.07199501991272 s
        # 13.15761399269104 s
        # return bubble_sort(self.random_int_list(-100, 1000, 1000))
        # 10.307480096817017 s
        # 11.329342126846313 s
        # 10.710936784744263 s
        # 11.044705629348755 s
        return insertion_sort( self.random_int_list(-100, 1000, 1000))

    def random_int_list(self, start, stop, length):
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        length = int(abs(length)) if length else 0
        random_list = []
        for i in range(length):
            random_list.append(random.randint(start, stop))
        return random_list


if __name__ == "__main__":
    demo = Demo()
    start = time.time()
    for i in range(100):
        rst = demo.run()
        # print(rst)
    print(f"use {time.time()-start} s")
