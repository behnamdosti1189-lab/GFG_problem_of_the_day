// Unique Subsets 

// https://practice.geeksforgeeks.org/problems/subsets-1587115621/1

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCases = sc.nextInt();
		for(int t=0;t<testCases;t++){
		    int n = sc.nextInt();
		    int arr[] = new int[n];
		    for(int i=0;i<n;i++){
		        arr[i] = sc.nextInt();
		    }
		    Arrays.sort(arr);
		    System.out.print("()");
		    ArrayList <ArrayList<Integer>> res = new solve().AllSubsets(arr,n);
		    for (int i = 0; i < res.size (); i++)
		    {
		        System.out.print ("(");
		        for (int j = 0; j < res.get(i).size (); j++)
		        {
		            if (j != res.get(i).size()-1)
		                System.out.print ((res.get(i)).get(j) + " ");
		            else
		                System.out.print ((res.get(i)).get(j));
		        }
		        System.out.print (")");
		      
		    }
		    System.out.println();
		}
	}
}// } Driver Code Ends


class solve
{
    //Function to find all possible unique subsets.
    public static ArrayList <ArrayList <Integer>> AllSubsets(int arr[], int n)
    {
        Arrays.sort(arr);
        ArrayList<ArrayList<Integer>> ans=new ArrayList<>();
        getSet(arr,new ArrayList<Integer>(),n,ans,0);
        ans.remove(0);
        return ans;
    }
    public static void getSet(int []arr,ArrayList<Integer> ls,int n,ArrayList<ArrayList<Integer>> ans,
    int ind){
      ans.add(new ArrayList<>(ls));
        for(int i=ind;i<n;i++){
            if(i!=ind&&arr[i]==arr[i-1]) continue;
            ls.add(arr[i]);
            getSet(arr,ls,n,ans,i+1);
            ls.remove(ls.size()-1);
        }
    }
}