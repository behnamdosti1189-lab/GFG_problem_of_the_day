// Min Coin 

// Given a list of coins of distinct denominations and total amount of money. Find the minimum number of coins required to make up that amount. Output -1 if that money cannot be made up using given coins.

// https://practice.geeksforgeeks.org/problems/min-coin5549/1#

// { Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String S = br.readLine().trim();
            String[] S1 = S.split(" ");
            int n = Integer.parseInt(S1[0]);
            int amount  = Integer.parseInt(S1[1]);
            String s = br.readLine().trim();
            String[] s1 = s.split(" ");
            int[] nums = new int[n];
            for(int i = 0; i < s1.length; i++)
                nums[i] = Integer.parseInt(s1[i]);
            Solution ob = new Solution();
            int ans = ob.MinCoin(nums, amount);
            System.out.println(ans);           
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
    public int MinCoin(int[] nums, int amount)
    {
       int dp[] = new int[amount+1];
       Arrays.fill(dp, Integer.MAX_VALUE);
       dp[0] = 0;
       for(int amt=0; amt<=amount; amt++){
          int min = Integer.MAX_VALUE;
          for(int coin : nums)
              if(coin <= amt)min = Integer.min(min, dp[amt-coin]);
          
          if(min != Integer.MAX_VALUE)dp[amt] = 1 + min;
       }
       
       return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
}