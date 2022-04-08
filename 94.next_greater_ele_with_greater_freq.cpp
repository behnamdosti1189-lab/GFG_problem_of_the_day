// Next element with greater frequency 

// Given an array arr[ ] of n integers, for every element, find the closest element on 
// it's right that has a greater frequency than its own frequency.

// https://practice.geeksforgeeks.org/problems/9656e96f6eaee49e67400fa2aed7833c8d9846b8/1#


// { Driver Code Starts
#include <bits/stdc++.h>
#define N 10000
using namespace std;


 // } Driver Code Ends

class Solution{
public:
    vector<int> print_next_greater_freq(int arr[],int n)
    {
        // code here
        stack<int> s;
        s.push(0);
        vector<int> res(n, -1);
        unordered_map<int, int> freq;
        for(int i=0; i<n; i++) freq[arr[i]]++;
        
        for(int i=1; i<n; i++){
            if(freq[arr[s.top()]] > freq[arr[i]]){
                s.push(i);
            }else{
                while(!s.empty() && freq[arr[s.top()]] < freq[arr[i]]){
                    res[s.top()] = arr[i];
                    s.pop();
                }
                s.push(i);
            }
        }
        return res;
    }
};



// { Driver Code Starts.

int main()
{
    int arr[N];
    
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        for(int i=0; i<n; i++)
            cin>>arr[i];
        
        Solution ob;
        vector<int> ans=ob.print_next_greater_freq(arr,n);
        for(auto x:ans){
            cout<<x<<" ";
        }
        cout << endl;
    }
	return 1;
}
  // } Driver Code Ends