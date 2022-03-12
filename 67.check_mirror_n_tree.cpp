// Check Mirror in N-ary tree 

// Given two n-ary trees. Check if they are mirror images of each other or not. 
// You are also given e denoting the number of edges in both trees, and two arrays, A[] and B[]. 
// Each array has 2*e space separated values u,v denoting an edge from u to v for the both trees.

// https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1#

// Very easy approach for each parrent its node should be in reverse order for second tree
// so first add the nodes in stack and the pop and check with other tree

// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int checkMirrorTree(int n, int e, int A[], int B[]) {
        // code here
        unordered_map<int, stack<int>> mp;
        for(int i=0;i<2*e;i+=2){
            mp[A[i]].push(A[i+1]);
        }
        for(int j=0;j<2*e;j+=2){
            if(mp[B[j]].top()!=B[j+1]){
                return 0;
            }
            mp[B[j]].pop();
        }
        
        return 1;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n,e;
        
        cin>>n>>e;
        int A[2*e], B[2*e];
        
        for(int i=0; i<2*e; i++)
            cin>>A[i];
            
        for(int i=0; i<2*e; i++)
            cin>>B[i];

        Solution ob;
        cout << ob.checkMirrorTree(n,e,A,B) << endl;
    }
    return 0;
}  // } Driver Code Ends