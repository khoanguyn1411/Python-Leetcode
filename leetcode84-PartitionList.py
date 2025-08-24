# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def transfer_list_to_linked_list(list: List[int]):
    temp = ListNode(1)
    dummy = temp
    for num in list:
        temp.next = ListNode(num)
        temp = temp.next
    temp = dummy.next
    dummy.next = None
    return temp


class Solution:
    def partition(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        l1 = ListNode(0)
        temp1 = l1
        l2 = ListNode(0)
        temp2 = l2

        cur = head

        while cur:
            if cur.val < target:
                temp1.next = ListNode(cur.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(cur.val)
                temp2 = temp2.next

            cur = cur.next

        temp1.next = l2.next
        return l1.next


ll = transfer_list_to_linked_list([1, 4, 3, 2, 5, 2], 3)
print(Solution().partition(ll))
