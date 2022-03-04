// Can Make Triangle 

// Given an array A[] of N elements, You'd like to know how many triangles can be formed with side lengths equal to adjacent elements from A[].

// Construct an array of integers of length N - 2 where ith element is equal to 1 if it is possible to form a triangle with side lengths A[i], A[i+1], and A[i+2]. otherwise 0.

// Note: A triangle can be formed with side lengths a, b and c if a+b>c and a+c>b and b+c>a.

// https://practice.geeksforgeeks.org/problems/51b7f8fb8b33d657a857f230361b7dad6565ce62/1#

// { Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
//User function Template for C++
class Solution
{
    public:
    bool check(int a,int b,int c)
    {
    	if(a + b > c and a + c > b and b + c > a)
    		return true;
    	return false;
    }
    	
    vector<int> canMakeTriangle(vector<int> A, int N)
    {
        // code here
        vector<int> res;
        for(int i = 0;i < A.size() - 2;i++)
        {
        	if(check(A[i],A[i+1],A[i+2]))
        		res.push_back(1);
        	else
        		res.push_back(0);
        }
        return res;
    }
};

// { Driver Code Starts.
int main() 
{ 
    int t;cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        vector<int> A(N);
        for(int i=0;i<N;i++)
            cin>>A[i];
        Solution ob;
        auto ans = ob.canMakeTriangle(A, N);
        for(int i=0;i<ans.size();i++)
            cout << ans[i] << " ";
        cout << endl;
        
    }

    return 0; 
}   // } Driver Code Ends