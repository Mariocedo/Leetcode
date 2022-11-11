# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_s = ""
        while head:
            list_s = list_s + str(head.val)
            head = head.next

        hlength = list_s.__len__() // 2 + list_s.__len__() % 2

        return list_s[0:hlength] == list_s[-hlength:][::-1]
