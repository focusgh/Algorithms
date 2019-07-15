#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List
)


def selection_sort(collection: List[int]) -> List[int]:
    """
    选择排序
    """
    length = len(collection)
    for i in range(length - 1):
        min_index = i + 1
        for j in range(i, length):
            if collection[j] < collection[min_index]:
                min_index = j
        # swap
        if min_index != i:
            collection[min_index], collection[i] = collection[i], collection[min_index]
    return collection


if __name__ == "__main__":
    test_list = [4, 5, -6, 1, 2, 3]
    print(selection_sort(test_list))
