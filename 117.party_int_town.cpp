// Party in Town 

// https://practice.geeksforgeeks.org/problems/party-in-town3951/1

class Solution{
public:
   int maxd =0;
    void dfs(int ind, vector<vector<int>>&adj, vector<int>&vis, int c){
        vis[ind]=1;
         maxd = max(maxd,c);  // max depth to which a node goes
        for(int i : adj[ind]){
            if(!vis[i]){
                dfs(i,adj,vis,c+1);
            }
        }
    }
    int partyHouse(int N, vector<vector<int>> &adj){

        int mx=INT_MAX;
        int house =-1;
         
        for(int i=1;i<=N;i++){
           vector<int>vis(N+1,0);
            maxd=0;
            dfs(i,adj,vis,0);  // for each find maxdeptht to which it goes and finally find min of it
            
            if(maxd<mx){ mx = maxd; 
           }
            
          }
        return mx;
    }
};
