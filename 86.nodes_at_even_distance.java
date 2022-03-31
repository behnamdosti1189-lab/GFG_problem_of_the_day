// { Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class GFG{
	public static void main(String [] args) throws IOException{
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0)
        {
            int n = sc.nextInt();
            ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

            for(int i = 0; i <= n; i++) {
            	graph.add(new ArrayList<>());
            }
            
            int temp = n;
            while(temp-- > 1){
                int u = sc.nextInt();
                int v = sc.nextInt();
                graph.get(u).add(v);
                graph.get(v).add(u);
            }
            Solution ob = new Solution();
            System.out.println(ob.countOfNodes(graph, n));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    int countOfNodes(ArrayList<ArrayList<Integer>> graph, int n) 
    {
       boolean []vis=new boolean[n+1];
       int []dist=new int[n+1];
       vis[1]=true;
       dist[1]=0;
       dfs(1,graph,dist,vis,1);
       int evn=0,odd=0;
       for(int i=1;i<=n;i++){
           if(dist[i]%2==0) evn++;
           else odd++;
       }
       return (evn*(evn-1)/2+odd*(odd-1)/2);
    }
    public void dfs(int s,ArrayList<ArrayList<Integer>> graph,int []dist,boolean []vis,int c){
         for(int i:graph.get(s)){
             if(!vis[i]){
                 dist[i]=c;
                 vis[i]=true;
                 dfs(i,graph,dist,vis,c+1);
             }
         }        
    }
}
