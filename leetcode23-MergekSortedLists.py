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
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         dummy = ListNode(-1)
#         temp = dummy
#         total_node = 0

#         lists = [l for l in lists if l]

#         for index, list in enumerate(lists):
#             cloned_head = list
#             while cloned_head:
#                 total_node += 1
#                 cloned_head = cloned_head.next

#         for i in range(total_node):
#             min_val_list = None
#             min_list_index = 0
#             for index, list in enumerate(lists):

#                 if not list:
#                     continue

#                 if not min_val_list:
#                     min_val_list = list
#                     min_list_index = index
#                 elif min_val_list.val >= list.val:
#                     min_val_list = list
#                     min_list_index = index

#                 if index == len(lists) - 1:
#                     if not min_val_list.next:
#                         lists.pop(min_list_index)
#                     else:
#                         lists[min_list_index] = min_val_list.next
#                     temp.next = ListNode(min_val_list.val)
#                     temp = temp.next

#         return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList.append(self.merge2Lists(l1, l2))
            lists = mergedList
        return lists[0]

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next

        current.next = l2 if not l1 else l1
        return dummy.next


l1 = transfer_list_to_linked_list([1, 4])
l2 = transfer_list_to_linked_list([1, 3])
l3 = transfer_list_to_linked_list([])
l4 = transfer_list_to_linked_list([-9, -8, -5, -3, -2, 0, 0, 3])
l5 = transfer_list_to_linked_list([-3, -3, 1, 2, 3, 3])
l6 = transfer_list_to_linked_list([-10, 4])

solution = Solution()
# print(solution.mergeKLists([l1, l2]).val)
print(solution.mergeKLists([l1, l2, l3, l4, l5, l6]
                           ).next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.val)
