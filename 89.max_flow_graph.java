// { Driver Code Starts
// Initial Template for Java
// Find the Maximum Flow 
// 
// Given a graph with N vertices numbered 1 to N and M edges, The task is to find the max flow from vertex 1 to vertex N.
// 
// In a flow network, the maximum flow of a path can't exceed the flow-capacity of an edge in the path.
// 
// https://practice.geeksforgeeks.org/problems/find-the-maximum-flow2126/1#
// 
// REALLY GFG I WANT THE REASON WHY MY COMMENT GOT DELETED
// 
// IM DOING FOR COMMUNITY AND YOU ARE DOING PARTIALITY 
// 
// NO WORRIES I WILL DO IT AGAIN
// 
// OKAY TO SOLVED THIS QUESTION I TAKE ALMOST 3.5+HR .BECAUSE I MIGHT BE THE SLOW CODER ,SO FOR THE TIME SAVING FOR U FELLOWS JUST FOLLOW MY STEPS TO GET THIS HARD ALGO . I KNOW THIS WILL TAKE TIME  BUT ATLAST YOU GOT SOMETING TO LEARN
// 
// 1-→ https://youtu.be/NwenwITjMys WATCH AT 1.25X SPEED
// 
// 2-→ https://youtu.be/KChvn4SNE4g WATCH AT 1.25-1.5X SPEED (WATCH LAST 4 MIN CAREFULLY)
// 
// 3-→ https://youtu.be/w0-c8io12yY  WATCH AT 1.25X SPEED 
// 
// 4-→ https://youtu.be/_aWooet7O_4 WATCH AT 1.25-1.5X SPEED (WATCH LAST 10MIN CAREFULLY)
// 
// 5-→ AT LAST JUST GO THROUGH THE https://cp-algorithms.com/graph/edmonds_karp.html
// 
// OTHER DOCUMENTATION https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/ ,,,https://www.geeksforgeeks.org/max-flow-problem-introduction/
// 
// HOPE THIS COMMET DO NOT GET DELETED AGAIN

import java.io.*;
import java.util.*; 
class GFG{
    public static void main(String args[]) throws IOException { 
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        
        while(t-- > 0){
    
            String input_line[] = read.readLine().trim().split("\\s+");
            int N = Integer.parseInt(input_line[0]);
            int M = Integer.parseInt(input_line[1]);
            
            ArrayList<ArrayList<Integer>> Edges = new ArrayList<ArrayList<Integer>>();
            input_line = read.readLine().trim().split("\\s+");
            for(int i=0;i<M;i++)
            {
                ArrayList<Integer> e = new ArrayList<Integer>();
                e.add(Integer.parseInt(input_line[3*i]));
                e.add(Integer.parseInt(input_line[3*i+1]));
                e.add(Integer.parseInt(input_line[3*i+2]));
                Edges.add(e);
            }
            Solution ob = new Solution();
            int ans = ob.solve(N, M, Edges); 
            System.out.println(ans);
        }
    } 
} // } Driver Code Ends


//User function Template for Java
class Solution 
{ 
    int solve(int n, int m, ArrayList<ArrayList<Integer>> edges) 
    { 
        int g[][] = new int[n][n];
        for(int i=0;i<edges.size();i++){
            int u = edges.get(i).get(0)-1;
            int v = edges.get(i).get(1)-1;
            int w = edges.get(i).get(2);
            g[u][v]+=w;
            g[v][u]+=w;
        }
        return fordfulkerson(g,0,n-1,n);
    }
    static int fordfulkerson(int[][]graph,int source,int sink,int n){
        int[]parent=new int[n];
        Arrays.fill(parent,-1);
        int res=0;
        while(bfs(graph,parent,source,sink,n)!=0){
            int min=bfs(graph,parent,source,sink,n);
            res+=min;
            int v=sink;
            while(v!=source){
                int u=parent[v];
                graph[u][v]-=min;
                graph[v][u]+=min;
                v=u;
            }
        }
        return res;
    }
    static int bfs(int[][]graph,int[] parent,int source,int sink,int n){
        int min=Integer.MAX_VALUE;
        Arrays.fill(parent,-1);
        parent[source]=-2;
        boolean[]vis=new boolean[n];
        Queue<pair>q=new LinkedList<>();
        q.add(new pair(source,min));
        while(!q.isEmpty()){
            pair curr=q.poll();
            int node =curr.x;
            int flow=curr.y;
            for(int i=0;i<n;i++){
                if(graph[node][i]!=0){
                    if(parent[i]==-1){
                        parent[i]=node;
                        int new_flow=Math.min(flow,graph[node][i]);
                        if(i==sink)return new_flow;
                        q.add(new pair(i,new_flow));
                    }
                }
            }
        }
        return 0;
    }
}


class pair{
    int x,y;
    public pair(int x,int y){
        this.x=x;
        this.y=y;
    }
}