// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

/* Link list node */
struct Node {
	int data;
	struct Node *next;
	Node(int x) {
		data = x;
		next = NULL;
	}
};

/* Function to print linked list */
void printList(struct Node *head)
{
	struct Node *temp = head;
	while (temp != NULL)
	{
		printf("%d ", temp->data);
		temp = temp->next;
	}
}




 // } Driver Code Ends
//User function Template for C++

/*Link list node
struct Node {
	int data;
	struct Node *next;
	Node(int x) {
		data = x;
		next = NULL;
	}
	
	Very Easy c++ code and explanation:

step1:

insertion sort??

insert an element on correct position in sorted array

at start len ==1 array always be sorted and we can start with second element and keep going for sorted array and make sorted array till ith pos.

and fit i+1 element on its correct pos.

 

step2:

code (given below)
};*/

class Solution
{
    public:
    Node* insertionSort(struct Node* head)
   {
       Node *curr=head->next;
       Node *prev=head;
       while(curr!=NULL){
           Node *temp=head;
           bool flag=true;
           while(temp!=curr){
               if(temp->data>curr->data){
                   swap(temp->data,curr->data);
                   flag=false;
                   break;
               }
               temp=temp->next;
           }
           if(flag) curr=curr->next;
       }
       return head;
   }
    
};

// { Driver Code Starts.
int main()
{
	int T;
	cin >> T;

	while (T--)
	{
		int n;
		cin >> n;

		Node *head = NULL;
		Node *temp = head;

		for (int i = 0; i < n; i++) {
			int data;
			cin >> data;
			if (head == NULL)
				head = temp = new Node(data);
			else
			{
				temp->next = new Node(data);
				temp = temp->next;
			}
		}

        Solution ob;

		head = ob.insertionSort(head);
		printList(head);

		cout << "\n";



	}
	return 0;
}  // } Driver Code Ends