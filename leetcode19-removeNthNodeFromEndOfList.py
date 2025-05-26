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
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Delete the nth node
        slow.next = slow.next.next

        return dummy.next


l1 = transfer_list_to_linked_list([1, 2, 3, 4, 5])

solution = Solution()
print(solution.removeNthFromEnd(l1, 2).val)
