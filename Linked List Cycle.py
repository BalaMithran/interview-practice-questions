
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow , fast =head , head
        while fast!=None and fast.next !=None and fast.next.next !=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        return False
        
