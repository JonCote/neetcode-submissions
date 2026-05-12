# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        setlen = 0
        curr = head

        while curr.next:
            visited.add(curr)
            if setlen == len(visited):
                return True

            setlen += 1
            curr = curr.next

        return False