// Robots 

// There are two kinds of bots A and B in a 1-D array. A bot can only move left while B can only move right. There are also empty spaces in between represented by #. But its also given that the bots cannot cross over each other.

// Given the initial state and final state, we should tell if the transformation is possible.

// NOTE: There can be many bots of the same type in a particular array. 

// https://practice.geeksforgeeks.org/problems/d35adfbe367861ec1e67bea6e0efebe0a0ee3550/1#

// https://www.youtube.com/watch?v=H7FLUtmce2Q

// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;


 // } Driver Code Ends
//User function Template for Java

class Solution{
    public static String moveRobots(String s1, String s2){
        //code here
        int i=0,j=0,n=s1.length();
        while(i<n && j<n){
            if(s1.charAt(i)=='#') i++;
            else if (s2.charAt(j)=='#') j++;
            else if (s1.charAt(i)!=s2.charAt(j)) return "No";
            else if (s1.charAt(i)=='A' && i<j) return "No";
            else if (s1.charAt(i)=='B' && i>j) return "No";
            else{
                i++;
                j++;
            }
        }
        return "Yes";
    }
}


// { Driver Code Starts.

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            String s1=read.readLine();
            String s2=read.readLine();

            Solution ob = new Solution();
            System.out.println(ob.moveRobots(s1, s2));
        }
    }
}  // } Driver Code Ends