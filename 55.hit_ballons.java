Hit most Balloons 

You are given an infinite two-dimensional grid. 
There are N balloons placed at certain coordinates of the grid. 
You have an arrow with yourself, which you will be using to shoot the balloons. 
You can select any point on the grid as your starting point and any point on the grid as the target point. 
When you fire the arrow, all ballons lying on the shortest path between the starting point and target point will be burst. Given the coordinates of the N ballons in an array arr, your task is to find out the maximum number of balloons that you can fire in one arrow shot.

https://practice.geeksforgeeks.org/problems/4e75764f8f1638eb4f1c5478ca1986043e15e39a/1#

// { Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while (t-- > 0) {

            int N = Integer.parseInt(br.readLine().trim());

            int arr[][] = new int[(int)(N)][2];

            for (int j = 0; j < 2; j++) {
                String inputLine2[] = br.readLine().trim().split(" ");
                for (int i = 0; i < N; i++) {
                    arr[i][j] = Integer.parseInt(inputLine2[i]);
                }
            }
            Solution ob = new Solution();
            System.out.println(ob.mostBalloons(N, arr));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public int mostBalloons(int N, int arr[][]) {
        // Code here
        
        /*The logic is the balloons present on the line connecting
            start and target point bursts.To check if there are on the same line
            we calculate the slope of the line and store number of points present on the line
            Here slope is a double value . 
        */
        int ans=0;
        for(int i=0;i<N;i++) {
            int x1=arr[i][0],y1=arr[i][1];
            HashMap<Double,Integer> hm=new HashMap<>();
            int count=0;
            for(int j=0;j<N;j++) {
                int x2=arr[j][0],y2=arr[j][1];
                if(x1==x2 && y1==y2){
                    count++;
                    continue;
                }
                double slope=((double)(y2-y1)/(double)(x2-x1));
                hm.put(slope,hm.getOrDefault(slope,0)+1);
            }
            for(double z: hm.keySet()){
                ans=Math.max(ans,count+hm.get(z));
            }
        }
        return ans;
    }
}