// { Driver Code Starts
//Initial template for C++

// Excel Sheet | Part - 1 

// Given a positive integer N, return its corresponding column title as it would appear in an Excel sheet.
// For N =1 we have column A, for 27 we have AA and so on.

// Note: The alphabets are all in uppercase.

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{
    public:
    string ExcelColumn(int N)
    {
        // Your code goes here
        string ans = "";
        while(N > 0){
            ans.push_back('A' + (N-1)%26);
            N = (N - 1)/26;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        Solution ob;
        cout<<ob.ExcelColumn(n)<<endl;
    }
    return 0;
}
      // } Driver Code Ends