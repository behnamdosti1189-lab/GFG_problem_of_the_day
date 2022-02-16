// Find rectangle with corners as 1 

// Given a NxM binary matrix consisting of 0s and 1s. Find if there exists a rectangle/ square within the matrix whose all four corners are 1. 

// https://practice.geeksforgeeks.org/problems/253524a82f7b4561dc33ff637cd3b92c33d4f216/1#

// // { Driver Code Starts
// //Initial Template for Java

import java.io.*;
import java.util.*;
import java.util.HashMap; 
import java.util.HashSet; 

class GFG{
	public static void main(String args[]) throws IOException { 
		Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while(t > 0){
       		int rows=sc.nextInt();
       		int columns=sc.nextInt();
			
			int matrix[][]=new int[rows][columns];
          
        	for(int i=0; i<rows;i++){            
            	for(int j=0; j<columns;j++){
                	matrix[i][j]=sc.nextInt();
            	}
         	}

			Solution x = new Solution();
			if (x.ValidCorner(matrix)) 
				System.out.println("Yes"); 
			else
				System.out.println("No"); 
			t--;
		}
	} 
}
	


// } Driver Code Ends


//User function Template for Java

public class Solution {
	static boolean ValidCorner(int matrix[][]) 
	{ 
	    Set<Integer> c=new HashSet<>();
	    for(int i=0;i<matrix.length;i++){
	        Set<Integer> s=new HashSet<>();
	        for(int j=0;j<matrix[0].length;j++){
	            if(matrix[i][j]==1){
	                int it=i;
	                while(it>0){
	                    it--;
	                    if(c.contains(j)){
	                        if(s.contains(it))
    	                        return true;
	                        else
    	                       s.add(it);
	                    }
	                }
	                c.add(j);
	            }
	        }
	    }
	    return false;
	}
};
