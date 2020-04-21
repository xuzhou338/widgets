#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:08:05 2020

@author: Zhou
"""

from collections import deque

class BinaryTreeNode:
    """General implementation of binary tree"""
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>'

def bt_from_list(l):
    """Construct binary tree from list."""
    n = iter(l)
    tree = BinaryTreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = BinaryTreeNode(next(n))
            fringe.append(head.left)
            head.right = BinaryTreeNode(next(n))
            fringe.append(head.right)
        except StopIteration:
            break
    return tree

def max_depth(root):
    """Return the max depth of the binary tree using recursion"""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1