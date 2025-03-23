struct ListNode {
     int val;
   struct ListNode *next;
};
 



struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* current = head;
    struct ListNode* prev = NULL;
    struct ListNode* nxt;  
    
    while (current) {
        nxt = current->next;  // Save next node
        current->next = prev; // Reverse the link
        prev = current;       // Move prev forward
        current = nxt;        // Move current forward
    }
    
    return prev;  
}