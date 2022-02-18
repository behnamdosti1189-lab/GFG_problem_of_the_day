'''
Rearrange Geek and his Classmates 

Assume an first ele is A and Another ele is B, Both ele is < n . So if  element A is increase by B*n. So the ele becomes  (A + B*n) .

To Get First Ele A (Older Value in sense when array index Increase) : 
(A + B*n) % n =A

 
To Get Second Ele A (New Value to Assign a Right index ) : 
(A + B*n) / n = B

https://practice.geeksforgeeks.org/problems/47e5aa3f32aee9e0405f04960f37c8a562d96a2f/1#
'''
// { Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution {
  public:
    void prank(long long a[], int n){
       
       for(int i=0;i<n;i++)
       {
           a[i] = a[i] + (a[a[i]]%n)*n ;
       }
       
       for(int i=0;i<n;i++)
           a[i]/=n ;       
   }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        long long a[n];
        for(int i = 0 ;i<n;i++){
            cin>>a[i];
        }
        Solution ob;
        ob.prank(a,n);

        for(int i = 0;i<n;i++)
            cout<<a[i]<<" ";
        cout<<"\n";
    }
}

  // } Driver Code Ends