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


# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         # Helper to get the kth node from current node
#         def get_kth_node(curr, k):
#             while curr and k > 0:
#                 curr = curr.next
#                 k -= 1
#             return curr

#         dummy = ListNode(0)
#         dummy.next = head
#         group_prev = dummy

#         while True:
#             kth = get_kth_node(group_prev, k)
#             if not kth:
#                 break

#             group_next = kth.next
#             prev = group_next
#             curr = group_prev.next

#             # Reverse the group
#             while curr != group_next:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp

#             temp = group_prev.next
#             group_prev.next = kth
#             group_prev = temp

#         return dummy.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Helper to get the kth node from current node
        def get_kth_node(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            kth = get_kth_node(group_prev, k)

            if not kth:
                break

            group_next = kth.next
            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next


l1 = transfer_list_to_linked_list([1, 2, 3, 4])

solution = Solution()
print(solution.reverseKGroup(l1, 2))
