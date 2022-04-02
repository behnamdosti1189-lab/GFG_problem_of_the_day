// Move all zeros to the front of the linked list 

// Given a linked list, the task is to move all 0s to the front of the linked list. The order of all another element except 0 should be same after rearrangement.

// https://practice.geeksforgeeks.org/problems/move-all-zeros-to-the-front-of-the-linked-list/1

void moveZeroes(struct Node **head)
{
    Node* prev=*head;
    Node* find=*head;
    
    find=find->next;
    while(find!=NULL)
    {
        
        if(find->data==0)
        {
            prev->next=find->next;
            find->next=*head;
            *head=find;
            find=prev->next;
        }
        else
        {
            prev=find;
            find=find->next;
            
        }
            
    }
}