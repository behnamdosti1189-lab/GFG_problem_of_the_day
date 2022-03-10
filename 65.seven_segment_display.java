// 7 Segment Display 

// Using seven segment display, you can write down any digit from 0 to 9 using at most seven segments. Given a positive number N and then a string S representing a number of N digits. You have to rearrange the segments in this N digit number to get the smallest possible N digit number. This number can have leading zeros. You can not waste any segment or add any segment from your own. You have to use all of the segments of the given N digits.

// https://www.youtube.com/watch?v=i9JgycQWORk

// https://practice.geeksforgeeks.org/problems/7-segment-display0752/1#

// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N = Integer.parseInt(read.readLine());
            String S = read.readLine();

            Solution ob = new Solution();
            System.out.println(ob.sevenSegments(S,N));
        }
    }
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    static String sevenSegments(String S, int N)
    {
        // code here
        int segments[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 5};
        
        int total_segments = 0;
        for(int i=0; i<N; i++)
        {
            int ch = S.charAt(i)-'0';
            total_segments += segments[ch];
        }
        
        int a[] = new int[N];
        
        for(int i=0; i<N; i++)
        {
            a[i] = 2;
            total_segments-=2;
        }
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        map.put(6, 0);
        map.put(2, 1);
        map.put(5, 2);
        map.put(4, 4);
        map.put(3, 7);
        map.put(7, 8);
        
        
        int i = 0;
        
        while(total_segments>=4 && i<N)
        {
            a[i++] += 4;
            total_segments -= 4;
        }
        
        int j = N-1;
        
        while(total_segments>0 && j>=0)
        {
            int res = 7-a[j];
            int min_val = Math.min(total_segments, res);
            a[j] += min_val;
            total_segments -= min_val;
            j--;
        }
        
        StringBuilder ans = new StringBuilder();
        
        for(int x : a)
        {
            ans.append(map.get(x));
        }
        
        
        return ans.toString();
        
        
    }
};