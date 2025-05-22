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

#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         c1 = list1
#         c2 = list2
#         temp = dummy

#         if not c1 and not c2:
#             return dummy.next
#         if not c1 and c2:
#             return c2
#         if not c2 and c1:
#             return c1

#         while c1.next or c2.next:
#             if c1.val <= c2.val:
#                 if not c1.next:
#                     temp.next = c2
#                     break
#                 else:
#                     temp.next = ListNode(c1.val)
#                     temp = temp.next
#                     c1 = c1.next
#             else:
#                 if not c2.next:
#                     temp.next = c1
#                     break
#                 else:
#                     temp.next = ListNode(c2.val)
#                     temp = temp.next
#                     c2 = c2.next

#         if c1.val <= c2.val:
#             temp.next = c1
#             temp = temp.next
#             temp.next = c2
#         else:
#             temp.next = c2
#             temp = temp.next
#             temp.next = c1

#         return dummy.next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining elements
        current.next = list1 if list1 else list2

        return dummy.next


l1 = transfer_list_to_linked_list([-9, 3])
l2 = transfer_list_to_linked_list([5, 7])

solution = Solution()
print(solution.mergeTwoLists(l1, l2).next)
