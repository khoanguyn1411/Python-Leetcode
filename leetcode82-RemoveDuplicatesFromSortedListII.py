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
        dummy = ListNode(0, head)  # dummy before head
        prev = dummy               # last node before the current sequence
        curr = head

        while curr:
            # detect duplicates
            if curr.next and curr.val == curr.next.val:
                # skip all nodes with this value
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr
            else:
                # move prev pointer
                prev = curr
                curr = curr.next

        return dummy.next


ll = transfer_list_to_linked_list([1, 2, 3, 3, 4, 4, 5])
print(Solution().deleteDuplicates(ll))
