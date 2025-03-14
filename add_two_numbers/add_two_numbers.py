from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def LL_to_numbers(self, LL):
        list_of_ll = []
        while LL:
            list_of_ll.append(LL.val)
            LL= LL.next
        mapped_list = list(map(str, list_of_ll))
        num = "".join(reversed(mapped_list))
        return int(num)

    def numbers_to_LL (self, num):
        head = ListNode(int(num[-1]))
        current = head
        for i in range(len(num) - 2, -1, -1):
            current.next = ListNode(int(num[i]))
            current = current.next
        return head
        


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 linked lists -> need to get their numbers in reverse
        # i.e. 2->3->4 = 432
        l1 = self.LL_to_numbers(l1)
        l2 = self.LL_to_numbers(l2)
        result = l1 + l2
        result_list = self.numbers_to_LL(str(result))
        return result_list


        