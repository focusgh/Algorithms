#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List
)


def merge_sort(collection: List[int]) -> List[int]:
    """
    归并排序
    """
    length = len(collection)
    if length <= 1:
        return collection
    mid = length // 2
    left = merge_sort(collection[:mid])
    right = merge_sort(collection[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


if __name__ == "__main__":
    test_list = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    print(merge_sort(test_list))