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
    # 二叉树的层序遍历
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


def get_tree_by_preorder_and_inorder(preorder: list, inorder: list):
    # 根据前序和中序遍历构建二叉树

    def dfs(subpre: list, subin: list):
        if not subpre:
            return None
        head_val = subpre[0]
        idx = subin.index(head_val)
        head = TreeNode(head_val)
        head.lchild = dfs(subpre[1:idx + 1], subin[:idx])
        right_subpre = subpre[-(len(subin) - idx - 1):] if len(subin) - idx - 1 > 0 else []
        head.rchild = dfs(right_subpre, subin[idx + 1:])
        return head

    return dfs(preorder, inorder)


def get_tree_by_inorder_and_postorder(inorder: list, postorder: list) -> TreeNode:
    def dfs(subin: list, subpost: list):
        if not subin:
            return None
        head = TreeNode(subpost[-1])
        idx = subin.index(subpost[-1])
        head.lchild = dfs(subin[:idx], subpost[:idx])
        head.rchild = dfs(subin[idx + 1:], subpost[idx:-1])
        return head

    return dfs(inorder, postorder)


def build_binary_search_tree(sorted_nums):
    def dfs(sub_nums):
        if not sub_nums:
            return None
        head_index = len(sub_nums) // 2
        head = TreeNode(sub_nums[head_index])
        head.lchild = dfs(sub_nums[:head_index])
        head.rchild = dfs(sub_nums[head_index + 1:])
        return head

    return dfs(sorted_nums)


if __name__ == '__main__':
    r = get_test_tree()
    # post_order(r)
    layer_order(r)
