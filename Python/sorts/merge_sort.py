#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import (
    List
)


def merge_sort(collection: List[int]) -> List[int]:
    """
    归并排序

    数组切片方式
    """

    # 终止条件
    length = len(collection)
    if length <= 1:
        return collection

    # 取中间位置
    mid = length // 2
    # 递归前半部分
    left = merge_sort(collection[:mid])
    # 递归后半部分
    right = merge_sort(collection[mid:])
    # 合并数组
    return _merge(left, right)


def _merge(left: List[int], right: List[int]):

    # 循环将两个数组合并到 result 数组中
    result = []
    while left and right:
        # 每次循环将数组头部较小的一方，添加到 result 数组
        # 归并排序是否是稳定，取决如下这个判断。
        #   left[0] 较小或等于，都优先添加到 result 数组中。以保证稳定。
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 返回合并结果
    return result + left + right


if __name__ == "__main__":
    test_list = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    print(merge_sort(test_list))
