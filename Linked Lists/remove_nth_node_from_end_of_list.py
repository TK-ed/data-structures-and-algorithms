# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # brute force approach
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        itr = head
        while itr:
            count+=1
            itr = itr.next
        if count == 1:
            new_head = head.next
            return new_head
        res = count - n
        itr = head
        while itr:
            res-=1
            if res == 0:
                del_node = itr.next
                itr.next = itr.next.next
            itr = itr.next
            
        return head
    
    # optimized approach
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        if not fast: return head.next
        while fast.next!=None:
            slow = slow.next
            print(slow)
            fast = fast.next    
            print(fast)
        slow.next = slow.next.next
        return head