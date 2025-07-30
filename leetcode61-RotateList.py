# Definition for singly-linked list.
from typing import List, Optional


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


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        if not head.next:
            return head

        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        k = k % n

        for i in range(k):
            current = head
            prev = current
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            current.next = head
            head = current
        return head


ll = transfer_list_to_linked_list([0, 1, 2])
print(Solution().rotateRight(ll, 4).val)
