/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode * front = head;
        ListNode * next = nullptr;
        ListNode * prev = nullptr;

            
        while (front != nullptr){
            next = front->next;
            front->next = prev;
            prev = front;
            front = next; 
        }
      
        return prev; 
      } 
};