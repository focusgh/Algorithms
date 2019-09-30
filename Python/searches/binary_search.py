#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

import bisect

from typing import (
    List
)


def binary_search(sorted_collection: List[int], item: int) -> int:
    """
    二分查找（非递归实现）
    :param sorted_collection: 有序数组
    :param item: 所要查找的数据项
    :return: index or -1
    """

    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if current_item > item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return -1


def binary_search_by_recursion(sorted_collection: List[int], item: int) -> int:
    """
    二分查找（递归实现）

    :param sorted_collection: 有序数组
    :param item: 所要查找的数据项
    :return: index or -1
    """
    left = 0
    right = len(sorted_collection) - 1
    return _binary_search_by_recursion(sorted_collection, left, right, item)


def _binary_search_by_recursion(sorted_collection: List[int], left: int, right: int, item: int) -> int:
    """
    递归方式二分查找具体实现
    :param sorted_collection: 有序数组
    :param left: 数组起始位置
    :param right: 数组结束位置
    :param item: 所要查找的数据项
    :return: index or -1
    """
    if left > right:
        return -1

    midpoint = (left + right) // 2
    current_item = sorted_collection[midpoint]
    if current_item == item:
        return midpoint
    else:
        if current_item > item:
            return _binary_search_by_recursion(sorted_collection, left, midpoint - 1, item)
        else:
            return _binary_search_by_recursion(sorted_collection, midpoint + 1, right, item)


def binary_search_by_bisect(sorted_collection: List[int], item: int) -> int:
    """
    二分查找（使用 python 标准库 bisect 实现）

    reference:
        https://docs.python.org/zh-cn/3/library/bisect.html
        http://kuanghy.github.io/2016/06/14/python-bisect

    :param sorted_collection: 有序数组
    :param item: 要查找的数据项
    :return: index or -1
    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and item == sorted_collection[index]:
        return index
    return -1
