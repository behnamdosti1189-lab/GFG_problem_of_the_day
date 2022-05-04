// Hungry Pizza Lovers 

// Dominos Pizza has hungry customers waiting in the queue. Each unique order is placed by a customer at time x[i], and the order takes y[i] units of time to complete.

// https://practice.geeksforgeeks.org/problems/hungry-pizza-lovers3148/1

// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


vector<int> permute(vector<vector<int>> &arr, int n);


int main() {
    
    int t;cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<vector<int>> arr(n);
        
        for(int i=0;i<n;i++)
        {
            int a, b;
            cin>> a>> b;
            arr[i].push_back(a);
            arr[i].push_back(b);
        }
        
        vector<int> ans;
        ans = permute(arr, n);
        for(int i=0;i<n;i++)
            cout << ans[i] << "\n";
        
    }
    
	return 0;
}// } Driver Code Ends


vector<int> permute(vector<vector<int>> &arr, int n) {
    int i=1;
    for(auto &p:arr){
        p[0]=p[0]+p[1];
        p[1]=i++;
    }
    sort(begin(arr),end(arr));
    vector<int> res;
    for(auto &p:arr) res.push_back(p[1]);
    return res;
}