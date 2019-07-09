#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List,
)


def insertion_sort(collection: List[int]) -> List[int]:
    """
    插入排序
    """
    length = len(collection)
    for i in range(1, length):
        insertion_index = i
        while insertion_index > 0 and collection[insertion_index - 1] > collection[insertion_index]:
            collection[insertion_index - 1], collection[insertion_index] = \
                collection[insertion_index], collection[insertion_index - 1]
            insertion_index -= 1
    return collection


if __name__ == "__main__":
    test_list = [4, 15, 6, 1, -2, 3]
    print(insertion_sort(test_list))
