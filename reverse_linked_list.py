# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if not head: # If there is no head, return None because there is nothing to go next
            return None

        newHead = head # New head is the current head, but we will change it to the last node in the list
        if head.next:
            newHead = self.reverseList(head.next) # Recursively call the function again on the self node
            head.next.next = head # This is a loop, basically says A -> B but B -> A instead, so it's a reversal of the list
        head.next = None # Then set the current head's next to None, which will be the new tail of the list
        return newHead

# [1, 2, 3] -> [3, 2, 1] 