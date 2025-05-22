# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
from typing import List


def transfer_list_to_linked_list(list: List[int]):
    temp = ListNode(1)
    dummy = temp
    for num in list:
        temp.next = ListNode(num)
        temp = temp.next
    temp = dummy.next
    dummy.next = None
    return temp


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:

#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode()
#         current = dummy
#         carry = 0
#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry
#             carry = total // 10

#             current.next = ListNode(total % 10)
#             current = current.next

#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = 1 if total >= 10 else 0

            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1 = transfer_list_to_linked_list([2, 4, 3])
l2 = transfer_list_to_linked_list([5, 6, 4, 3])

solution = Solution()
print(solution.addTwoNumbers(l1, l2).next.next.next.val)
