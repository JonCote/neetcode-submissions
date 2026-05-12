# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        self.recHelper(list1, list2, merged_list)
        return merged_list.next



    def recHelper(self, list1: Optional[ListNode], list2: Optional[ListNode], merged_list: Optional[ListNode]):
        if list1 == None:
            merged_list.next = list2
            return
        elif list2 == None:
            merged_list.next = list1
            return
        elif list1.val < list2.val:
            merged_list.next = list1
            self.recHelper(list1.next, list2, merged_list.next)
        else:
            merged_list.next = list2
            self.recHelper(list1, list2.next, merged_list.next)