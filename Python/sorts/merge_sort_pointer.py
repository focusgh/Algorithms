#!/usr/bin/env python
# coding: utf-8
# __author__ = 'wang tao'

from typing import List


def merge_sort(col: List[int]):
    _merge_sort(col, 0, len(col) - 1)


def _merge_sort(col: List[int], left: int, right: int) -> None:
    """
    归并排序

    双指针方式
    """

    # 递归终止条件q
    if left == right:
        return

    # 取中间位置
    mid = (left + right) >> 1

    # 递归左半部分
    _merge_sort(col, left, mid)
    # 递归右半部分
    _merge_sort(col, mid + 1, right)
    # 合并
    _merge(col, left, mid, right)


def _merge(col: List[int], left: int, mid: int, right: int) -> None:
    i, j = left, mid + 1
    tmp = []

    # 将两部分数组内容合并到 tmp 数组中
    while i <= mid and j <= right:
        if col[i] <= col[j]:
            tmp.append(col[i])
            i += 1
        else:
            tmp.append(col[j])
            j += 1

    # 将剩余数据添加到 tmp 数组
    if i <= mid:
        tmp.extend(col[i: mid + 1])
    else:
        tmp.extend(col[j: right + 1])

    # 将 tmp 数据拷贝回原数组
    col[left: right + 1] = tmp


if __name__ == "__main__":
    test_list = [5, 1, 9, 3, 7, 8]
    print(test_list)
    merge_sort(test_list)
    print(test_list)
