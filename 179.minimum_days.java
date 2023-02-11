class Solution {
    public static int getMinimumDays(int N, String S, int[] P) {
        // code here
        char ar[] = S.toCharArray();
        int i = 1, j = 0;
        while (i < N && j < N) {
            if (ar[i] != '?' && ar[i] == ar[i - 1]) {
                ar[P[j]] = '?';
                j++;
            } else {
                i++;
            }
        }
        return j;
    }
}
