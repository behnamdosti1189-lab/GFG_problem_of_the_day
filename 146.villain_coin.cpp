

int minColour(int N, int M, vector<int> mat[]) {
        // code here
        vector<int> adj[N+1];
        vector<int> indegree(N+1, 0);
        for(int i = 0; i < M; i++) {
            int v = mat[i][1];
            int u = mat[i][0];
            adj[u].push_back(v);
            indegree[v]++;
        }
        
        queue<int> q;
        for(int i = 1; i <= N; i++) {
            if(indegree[i] == 0) {
                q.push(i);
            }
        }
        int count = 0;
        while(q.empty() == false) {
            count++;
            while(q.empty() == false) {
                int curr = q.front();
                q.pop();
                for(auto it: adj[curr]) {
                    indegree[it]--;
                }
                indegree[curr] = -1;
            }
            for(int i = 1; i <= N; i++) {
                if(indegree[i] == 0) {
                    q.push(i);
                }
            }        
        }
    
        return count;    
    }