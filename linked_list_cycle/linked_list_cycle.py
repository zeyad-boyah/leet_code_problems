# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        iterator1 = head
        iterator2 = head
        while iterator2 and iterator2.next:
            iterator1 = iterator1.next # normal speed iterator
            iterator2 = iterator2.next.next # double speed iterator
            if iterator1 == iterator2:
                return True
        return False

        