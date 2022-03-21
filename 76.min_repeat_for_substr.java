// Minimum times A has to be repeated such that B is a substring of it 

// Given two strings A and B. Find minimum number of times A has to be repeated such that B is a Substring of it. If B can never be a substring then return -1.

// https://practice.geeksforgeeks.org/problems/5ef42ba605fff6cd60b1b2dd2ee230ade1fa25b0/1#


// { Driver Code Starts
    import java.io.*;
    import java.util.*;
    
    class GFG {
        public static void main(String args[]) throws IOException {
            BufferedReader read =
                new BufferedReader(new InputStreamReader(System.in));
            int t = Integer.parseInt(read.readLine());
            while (t-- > 0) {
                String A = read.readLine();
                String B = read.readLine();
    
                Solution ob = new Solution();
                System.out.println(ob.minRepeats(A,B));
            }
        }
    }// } Driver Code Ends
    
    
    //User function Template for Java
    
    class Solution {
        static int minRepeats(String A, String B) {
            int count=1;
            String K=A;
            
            while(A.length()<=2*B.length())
            {
                int z=A.length();
                int z1=A.replace(B,"").length();
                if(z1!=z)
                return count;
                
                count++;
                A+=K;
            }
            return -1;
        }
    };