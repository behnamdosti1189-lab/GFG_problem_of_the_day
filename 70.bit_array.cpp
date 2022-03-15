Bitwise AND of the Array 

Given an array A[ ] of N integers and an integer X. In one operation, you can change the ith element of the array to any integer value where 1 ≤ i ≤ N. Calculate minimum number of such 
operations required such that the bitwise AND of all the elements of the array is strictly greater than X.

https://practice.geeksforgeeks.org/problems/5109f04a157ca54bbb373477b1afeec22e7f1812/1#

// { Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++
class Solution{
    public:
    int count(int N, vector<int> A,int X){
       int p = 0, ans = N;
       for(int i=31; i >= 0; i--){
           int bit = (X>>i) & 1;
           if(bit == 1){
               p = p | (1<<i);
           }
           else{
               int temp = p | (1<<i);
               int cnt = 0;
               for(auto ele: A){
                   if((ele&temp) == temp){
                       cnt++;
                   }
               }
               
               ans = min(ans,N-cnt);
           }
       }
       return (ans);
   }
};

// { Driver Code Starts.
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int N,X;
        cin>>N>>X;
        vector<int> A(N);
        for(auto &i:A)
            cin>>i;
        Solution obj;
        int ans = obj.count(N, A, X);
        cout<<ans<<endl;
    }
}  // } Driver Code Ends