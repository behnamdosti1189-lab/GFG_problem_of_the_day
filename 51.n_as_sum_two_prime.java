// Return two prime numbers 

// Given an even number N (greater than 2), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only the pair whose minimum value is the smallest among all the minimum values of pairs and print the minimum element first.

// NOTE: A solution will always exist, read Goldbachs conjecture. 

// https://practice.geeksforgeeks.org/problems/return-two-prime-numbers2509/1#

// using Sieve of Eratosthenes to fin prime numbers from 2 to n
// then checking if i and n-i is prime return them solution always exists

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
            int N = Integer.parseInt(in.readLine());
            
            Solution ob = new Solution();
            List<Integer> ans = new ArrayList<Integer>();
            ans = ob.primeDivision(N);
            System.out.println(ans.get(0) + " " + ans.get(1));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution{
    static List<Integer> primeDivision(int N){
        // code here
        boolean prime[] = new boolean[N+1];
        ArrayList<Integer> ans = new ArrayList<Integer>();
        Arrays.fill(prime,Boolean.TRUE);
        prime[0] = false;
        prime[1] = false;
        
        for(int p=2; p*p<=N; p++){
            if(prime[p]==true){
                for(int i=p*p; i<=N; i+=p){
                    prime[i] = false;
                }
            }
        }
        
        for(int i=2;i<prime.length;i++){
            if((prime[i]==true) && (prime[N-i]==true)){
                ans.add(i);
                ans.add(N-i);
            }
        }
        
        return ans;
    }
}