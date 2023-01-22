class Solution {
  public:
    int solve(int N, int K, vector<int> &arr) {
        // code here
        for(int i=1;i<N;i++) arr[i]+=arr[i-1];
        vector<int> factor;
        for(int i=1;i*i<=arr[N-1];i++) {
            if(arr[N-1]%i==0) {
                factor.push_back(i);
                factor.push_back(arr[N-1]/i);
            }
        }
        
        int ans=1;
        for(int fact : factor) {
            int count=0;
            for(int a : arr) {
                if(a%fact==0) {
                    count++;
                }
            }
            if(count>=K) ans=max(ans,fact);
        }
        return ans;
    }

};
