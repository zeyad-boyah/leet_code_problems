# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LL_len (head):
    current = head
    ll_len = 0
    while current:
        current = current.next
        ll_len += 1
    return ll_len

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ll_len = LL_len(head)
        current_element = head
        element_after = current_element.next or None
        # while change this element as i rearrange the LL initially it needs to be the first element in the LL
        element_to_be_modified = head
        # this is the number of times a pointer rearrangement has happened and max mode will come for this equation (len-1)/2
        modification_num = 0
        max_modification_num = int((ll_len-1)/2)
        if max_modification_num == 0:
            return

        while modification_num < max_modification_num:
            # if we reach the end of the LL
            if element_after.next == None:
                # some intense pointer logic i made with a white board 
                element_after.next = element_to_be_modified.next
                element_to_be_modified.next = element_after
                current_element.next = None
                element_to_be_modified = element_after.next 
                current_element = element_to_be_modified
                element_after = current_element.next
                modification_num += 1
            else:
                # LL navigation
                current_element = current_element.next
                element_after = element_after.next















"""
this solution will not satisfy the space complexly requirement of the problem so i need to find another solution by rearranging the already existing pointers
without creating an entirely new linked list :( :cry:
"""

'''class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        odd_counter= 0
        even_counter = 1
        LL_as_list = LL_to_list(head)
        LL_as_list_len = len(LL_as_list)
        ans_as_list = [None] * LL_as_list_len

        for i in range(LL_as_list_len):
            if i%2 == 0:
                ans_as_list[i] = LL_as_list[odd_counter] 
                odd_counter += 1
            else:
                ans_as_list[i] = LL_as_list[LL_as_list_len - even_counter] 
                even_counter += 1
        new_head = list_to_LL(ans_as_list)
        curr_old = head
        curr_new = new_head
        while curr_new:
            curr_old.val = curr_new.val
            curr_old = curr_old.next
            curr_new = curr_new.next

def LL_to_list(head):
    ans_list= []
    current = head
    while current:
        ans_list.append(current.val)
        current = current.next
    return ans_list

def list_to_LL (given_list):
    head = ListNode(given_list[0])
    current = head
    for i in range(1,len(given_list)-1, 1):
        current.next = ListNode(given_list[i])
        current = current.next
    return head'''
        

        