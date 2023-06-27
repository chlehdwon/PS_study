/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
	int getLength(ListNode *head){
		int len=0;
		while(head!=NULL){
			head = head->next;
			len++;
		}
		
		return len;
	}
	
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		if(headA==NULL || headB==NULL) return 0;
        ListNode& tempA = headA;
		ListNode& tempB = headB;
		int len_A = getLength(headA);
		int len_B = getLength(headB);
		int diff = len_A-len_B;
		
		if(diff>0)
			while(diff--)
				tempA = tempA->next;
		else
			while(diff++)
				tempB = tempB->next;
		
		while(tempA && tempB){
			if(tempA == tempB)
				return tempA->val;
			tempA=tempA->next;
			tempB=tempB->next;
		}
		
		return 0;
    }
};

/*
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode* pointerA = headA;
        ListNode* pointerB = headB;
        while(pointerA != pointerB)
        {
            if(pointerA != NULL)
            {
                pointerA = pointerA->next;
            }
            else
            {
                pointerA = headB;
            }
            if(pointerB != NULL)
            {
                pointerB = pointerB->next;
            }
            else
            {
                pointerB = headA;
            }
        }
        return pointerA;
    }
};
*/