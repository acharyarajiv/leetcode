# https://leetcode.com/problems/add-two-numbers/
# https://www.youtube.com/watch?v=LLPuC5kWD8U
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        node = self
        res = ''
        while node is not None:
            res = str(node.val) + ' -> ' + res
            node = node.next
        print(res[:-3])

class Solution:
    def addReverseTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_Node = None
        if l1.next is not None and l2.next is not None:
            res_Node = self.addTwoNumbers(l1.next, l2.next)
        elif l1.next is not None:
            node = ListNode(0)
            node.next = l2
            l2 = node
            res_Node = self.addTwoNumbers(l1.next, l2.next)
        elif l2.next is not None:
            node = ListNode(0)
            node.next = l1
            l1 = node
            res_Node = self.addTwoNumbers(l1.next, l2.next)

        if res_Node is not None:
            carry = res_Node.val
            res_Node = res_Node.next
        else:
            carry = 0
        total = carry + l1.val + l2.val
        carry = total // 10
        res = total % 10
        carryNode = ListNode(carry)
        carryNode.next = ListNode(res)
        carryNode.next.next = res_Node
        return carryNode

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res_node: ListNode = None
        temp_node = None
        while l1 is not None or l2 is not None:
            val1, val2 = 0, 0
            if l1 is not None:
                val1 = l1.val
                l1 = l1.next
            if l2 is not None:
                val2 = l2.val
                l2 = l2.next

            res = carry + val1 + val2
            carry = res // 10
            res = res % 10
            if res_node is None:
                res_node = ListNode(res)
                temp_node = res_node
            else:
                temp_node.next = ListNode(res)
                temp_node = temp_node.next
        if carry > 0:
            temp_node.next = ListNode(carry)
            temp_node = temp_node.next
        return res_node

def buildNode(num):
    i = 0
    arr = []
    num_node = None
    while num > 0:
        mod = num % 10
        num //= 10
        if num_node is None:
            node = ListNode(mod)
            num_node = node
        else:
            node.next = ListNode(mod)
            node = node.next
    return num_node

if __name__ == '__main__':
    num1 = buildNode(1)
    num2 = buildNode(99)
    res = Solution().addTwoNumbers(num1, num2)
    res.print()
