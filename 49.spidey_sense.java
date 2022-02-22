Spidey Sense 

Spiderman is stuck in a difficult situation. His arch-enemy the Green Goblin has planted several of his infamous Pumpkin Bombs in various locations in a building. Help Spiderman activate his Spidey Sense and identify the impact zones. 
He has a blueprint of the building which is a M x N matrix that is filled with the characters O, B, and W where: 
O represents an open space.
B represents a bomb.
W represents a wall.
You have to replace all of the Os (open spaces) in the matrix with their shortest distance from a bomb without being able to go through any walls. Also, replace the bombs with 0 and walls with -1 in the resultant matrix. If no path exists between a bomb and an open space replace the corresponding 'O' with -1.

https://practice.geeksforgeeks.org/problems/spidey-sense5556/1#

// { Driver Code Starts
    import java.util.*;
    import java.math.*;
    
    class Pair{
        
        int x,y;
        Pair(int x,int y)
        {
            this.x = x;
            this.y = y;
        }
    }
    
    class Gfg
    {
        public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = Integer.parseInt(sc.next());
            while(t-- > 0)
            {
                int m = Integer.parseInt(sc.next());
                int n = Integer.parseInt(sc.next());
                char mat[][] = new char[m][n];
                for(int i=0;i<m;i++)
                {
                    for(int j=0;j<n;j++)
                    {
                        mat[i][j] = sc.next().charAt(0);
                    }
                }
               
                Solution T = new Solution();
                int ans[][] = T.findDistance(mat, m, n);
                
                for(int i=0;i<m;i++)
                {
                    for(int j=0;j<n;j++)
                    {
                        System.out.print(ans[i][j] + " ");
                    }
                    System.out.println();
                }
            }
        }
    }
    // } Driver Code Ends
    
    
    class ThreePair{
       int row;
       int col;
       int time;
       ThreePair(int row, int col, int time){
           this.row=row;
           this.col=col;
           this.time=time;
       }
    }
    class Solution
    {
       public static int[][] findDistance(char mat[][], int n,int m)
       {
           int[][] ans=new int[n][m];
           Queue<ThreePair> q=new LinkedList<>();
           boolean[][] vis=new boolean[n][m];
           int mx=Integer.MAX_VALUE;
           for(int i=0;i<n;i++){
               for(int j=0;j<m;j++){
                   if(mat[i][j]=='W') {
                       ans[i][j]=-1;
                       vis[i][j]=true;
                   }
                   else if(mat[i][j]=='B') {
                       ans[i][j]=0;
                       q.add(new ThreePair(i,j,0));
                       vis[i][j]=true;
                   }
                   else ans[i][j]=mx;
               }
           }
           
           while(!q.isEmpty()){
               int k=q.size();
               for(int i=0;i<k;i++){
                   ThreePair t=q.poll();
                   int a=t.row;
                   int b=t.col;
                   int c=t.time;
                   int[] xidx=new int[]{-1, 0, 1, 0};
                   int[] yidx=new int[]{0, 1, 0, -1};
                   for(int j=0;j<4;j++){
                       int ni=a+xidx[j];
                       int nj=b+yidx[j];
                       if(ni>=0 && nj>=0
                               && ni<n && nj<m && mat[ni][nj]!=('W'|'B') && vis[ni][nj]==false ){
                           vis[ni][nj]=true;
                           ans[ni][nj]=c+1;
                           q.add(new ThreePair(ni,nj,c+1));
                       }
                   }
               }
           }
           for(int i=0;i<n;i++){
               for(int j=0;j<m;j++){
                   if(ans[i][j]==mx){
                       ans[i][j]=-1;
                   }
               }
           }
           return ans;
       }
    }