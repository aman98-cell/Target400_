class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):

        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False