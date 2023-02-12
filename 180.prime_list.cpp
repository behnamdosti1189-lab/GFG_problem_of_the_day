class Solution{
public:
    bool isPrime(int x ){
        if(x<=1) return false;
        for(int i=2;i*i<=x;i++){
            if(x%i==0){
                return false;
            }
        }
        return true;
    }
    Node *primeList(Node *head){
        Node* temp=head;
        while(temp!=NULL){
            int num=temp->val;
            int l=num;
            int r=num;
            while(l>=0 || r<num*num){
                if(isPrime(l)){
                    temp->val=l;
                    break;
                }
                if(isPrime(r)){
                    temp->val=r;
                    break;
                }
                l--;
                r++;
            }
            temp=temp->next;
        }
        return head;
    }
};
