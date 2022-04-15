// Maximum sum Rectangle 

// Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.

// https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1#

// { Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N, M, x, y;
            String S[] = read.readLine().split(" ");
            N = Integer.parseInt(S[0]);
            M = Integer.parseInt(S[1]);
            int a[][] = new int[N][M];
            for (int i = 0; i < N; i++) {
                String s[] = read.readLine().split(" ");
                for (int j = 0; j < M; j++) a[i][j] = Integer.parseInt(s[j]);
            }
            Solution ob = new Solution();
            System.out.println(ob.maximumSumRectangle(N, M, a));
        }
    }
}// } Driver Code Ends


// User function Template for Java

class Solution {
    int maximumSumRectangle(int r, int c, int m[][]) {
        // code here
        int max = Integer.MIN_VALUE;
        int [] dp = new int[c];
        for(int i=0;i<r;i++){
            for(int j=i;j<r;j++){
               for(int k=0;k<c;k++){
                   dp[k] += m[j][k]; 
               } 
               max = Math.max(max, kadane(dp));
            }
            Arrays.fill(dp, 0);
        }
        return max;
    }
    public static int kadane(int [] dp){
        int sum=dp[0], max=dp[0];
        for(int i=1;i<dp.length;i++){
            sum+= dp[i];
            if(sum<dp[i])
                sum = dp[i];
            max = Math.max(sum, max);
        }
        return max;
    }
}