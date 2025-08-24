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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val != cur.next.val:
                prev = cur
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur
                prev = cur
                cur = cur.next
        return dummy.next


ll = transfer_list_to_linked_list([1, 2, 3, 3, 4, 4, 5])
print(Solution().deleteDuplicates(ll))
