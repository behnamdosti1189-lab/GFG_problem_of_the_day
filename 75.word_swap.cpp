// Choose and Swap 
// Easy

// You are given a string s of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.

// https://practice.geeksforgeeks.org/problems/choose-and-swap0531/1#


// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
public:
    string chooseandswap(string a){
        // Code Here
        
        char bg='a';
        int i=0,j=0;
        map<char,int> m;
        for( i=0;i<a.length();i++){
            
            if(a[i]=='a'+j){
                m[a[i]]++;
                j++;
                while(a[i]==a[i+1])
                    i++;
                continue;}
            else if(a[i]=='a'){
                j=1;
                continue;
                
            }
            break;
        }
        //cout<<i<<endl;
        if(i==a.length())
            return a;
        char f2=a[i];
        char f1=a[i];
        bool cv=false;
        //cout<<ch<<endl;
        for(int x=i;x<a.length();x++){
            f1=a[x];
            f2=a[x];
            //cout<<"f1 is"<<f1<<endl;
        for(int z=x+1;z<a.length();z++){
            //cout<<"loop startes"<<endl;
           //cout<<a[i]<<endl;
            if(a[z]<f2&&m[a[z]]==0){
                f2=a[z];
                //cout<<"f2 updated "<<f2<<endl;
                cv=true;
                
            }
        }
        m[a[x]]++;
        if(cv==true)
            break;
        }
        //cout<<f1<<endl<<f2<<endl;
        for(int i=0;i<a.length();i++){
            if(a[i]==f1)
                a[i]=f2;
            else if(a[i]==f2)
                a[i]=f1;
        }
        return a;
    }
    
};


// { Driver Code Starts.

int main()
{
    Solution obj;
	int t;
	cin >> t;
	while(t--)
	{	
	    string a;
		cin >> a;
		cout << obj.chooseandswap(a) << endl;
	}
	return 0;
}
  // } Driver Code Ends
