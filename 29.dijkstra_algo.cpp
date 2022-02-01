
// Implementing Dijkstra Algorithm 

// Given a weighted, undirected and connected graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S.
// Note: The Graph doesn't contain any negative weight cycle.

// https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1#

// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Node {
  public:
    int data;
    int cost;
    
    Node(int data, int cost) {
        this->data = data;
        this->cost = cost;
    }
};

class MyComp {
  public:
    bool operator() (Node a, Node b) {
        return a.cost > b.cost;
    };
};

class Solution {
	public:
	//Function to find the shortest distance of all the vertices
    //from the source vertex S.
    
    vector<int> dijkstra(int V, vector<vector<int>> adj[], int S) {
        priority_queue<Node, vector<Node>, MyComp> pQueue;
        
        vector<int> ans(V, 0);
        unordered_set<int> done;
        
        pQueue.push({S, 0});
        while(!pQueue.empty()) {
            auto cur = pQueue.top(); pQueue.pop();
            if(done.count(cur.data)) continue;
            done.insert(cur.data);
            ans[cur.data] = cur.cost;
            for(auto it: adj[cur.data]) {
                if(!done.count(it[0]))
                    pQueue.push({it[0], it[1] + cur.cost});
            }
        }
        
        return ans;
    }
};

// { Driver Code Starts.


int main()
{
    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;
        vector<vector<int>> adj[V];
        int i=0;
        while (i++<E) {
            int u, v, w;
            cin >> u >> v >> w;
            vector<int> t1,t2;
            t1.push_back(v);
            t1.push_back(w);
            adj[u].push_back(t1);
            t2.push_back(u);
            t2.push_back(w);
            adj[v].push_back(t2);
        }
        int S;
        cin>>S;
        
        Solution obj;
    	vector<int> res = obj.dijkstra(V, adj, S);
    	
    	for(int i=0; i<V; i++)
    	    cout<<res[i]<<" ";
    	cout<<endl;
    }

    return 0;
}

  // } Driver Code Ends