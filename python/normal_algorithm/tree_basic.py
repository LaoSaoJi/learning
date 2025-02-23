#  -*- coding: utf-8 -*-
"""
Author: sanjin
基础的树相关算法
"""
from typing import Optional


class TreeNode(object):

    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

    def print(self):
        print(f"{self.val} ")


def get_test_tree():
    vals = [0, 1, 2, 3, 4, 5]
    nodes = []
    for val in vals:
        nodes.append(TreeNode(val))
    nodes[3].lchild = nodes[1]
    nodes[1].lchild = nodes[0]
    nodes[1].rchild = nodes[2]
    nodes[3].rchild = nodes[5]
    nodes[5].lchild = nodes[4]
    return nodes[3]


def pre_order_circle(root: Optional[TreeNode]):
    # 循环实现前序遍历
    if not root:
        return
    queue = [root]
    while queue:
        cur = queue.pop()
        cur.print()
        if cur.rchild:
            queue.append(cur.rchild)
        if cur.lchild:
            queue.append(cur.lchild)


def pre_order(node: Optional[TreeNode]):
    if not node:
        return
    node.print()
    pre_order(node.lchild)
    pre_order(node.rchild)


def mid_order(node: Optional[TreeNode]):
    if not node:
        return
    mid_order(node.lchild)
    node.print()
    mid_order(node.rchild)


def post_order(node: Optional[TreeNode]):
    if not node:
        return
    post_order(node.lchild)
    post_order(node.rchild)
    node.print()


def layer_order(node: Optional[TreeNode]):
    if not node:
        return
    queue = [node]
    while queue:
        cur = queue[0]
        cur.print()
        queue = queue[1:]
        if cur.lchild:
            queue.append(cur.lchild)
        if cur.rchild:
            queue.append(cur.rchild)


if __name__ == '__main__':
    r = get_test_tree()
    # post_order(r)
    layer_order(r)
