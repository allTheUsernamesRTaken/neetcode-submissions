# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i =0
        result = ListNode()
        def single(l,carry):
            newCarry=0
            if(l is None):
                if(carry==0):
                    return None
                else:
                    return ListNode(1)
            else:
                if(l.val+carry>=10):
                    newCarry=1
                return ListNode((l.val+carry)%10,single(l.next,newCarry))

        def help(a,b,carry):
            newCarry=0
            if(a is None and b is None):
                if(carry==1):
                    return ListNode(1)
                return None
            if(b is None):
                return single(a,carry)
            elif(a is None):
                return single(b,carry)
            else:
                if(a.val+b.val+carry>=10):
                    newCarry=1
                return ListNode((a.val+b.val+carry)%10, help(a.next,b.next,newCarry))
            
        return help(l1,l2,0)
            

        