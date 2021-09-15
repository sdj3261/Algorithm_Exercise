# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        num1 = num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        sum = str(int(num1[::-1]) + int(num2[::-1]))

        sum = sum[::-1]
        curr = answer

        for i in range(len(sum)):
            curr.next = ListNode()
            curr = curr.next
            curr.val = sum[i]

        return answer.next


