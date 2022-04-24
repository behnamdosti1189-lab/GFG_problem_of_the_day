// # Product of Primes 

// # https://practice.geeksforgeeks.org/problems/product-of-primes5328/1#

// # Same solution in python is not accepted dont know !!

// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String a[] = in.readLine().trim().split("\\s+");
            long L = Long.parseLong(a[0]);
            long R = Long.parseLong(a[1]);
            
            Solution ob = new Solution();
            System.out.println(ob.primeProduct(L, R));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    
    static long primeProduct(long L, long R)
    {
        boolean prime[] = new boolean[(int)R+1];
        
        Arrays.fill(prime, true);
    
    
        for(int i=2; i*i<=R; i++)
        {
            if(prime[i])
            {
                for(int j=i*i; j<=R; j+=i)
                {
                    prime[j] = false;
                }
            }
        }
        
        long ans = 1l;
        
        for(int i=(int)L; i<=R; i++)
        {
            if(prime[i])
            {
                ans = (ans*i)%1000000007;
            }
        }
        
        
        return ans;
    }
}