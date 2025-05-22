# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# It is guaranteed that the list represents a number that does not have leading zeros.

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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_node = 0
        cloned_head = head
        while cloned_head:
            total_node += 1
            cloned_head = cloned_head.next
        if total_node < n:
            return None
        if total_node == n:
            head = head.next
            return head
        current = head
        for i in range(total_node - n - 1):
            current = current.next
        print(current.val)
        removed_node = current.next
        current.next = removed_node.next
        removed_node.next = None
        return head


l1 = transfer_list_to_linked_list([1, 2])

solution = Solution()
print(solution.removeNthFromEnd(l1, 2).val)
