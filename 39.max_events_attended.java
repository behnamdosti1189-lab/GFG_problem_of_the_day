// Maximum number of events that can be attended 

// There are N events in Geek's city. You are given two arrays start[] and end[] denoting starting and ending day of the events respectively. Event i starts at start[i] and ends at end[i].
// You can attend an event i at any day d between start[i] and end[i] (start[i] ≤ d ≤ end[i]). But you can attend only one event in a day.
// Find the maximum number of events you can attend.

// https://practice.geeksforgeeks.org/problems/ea8230731ccb057120bafb351c10c48b2d496125/1#

class Solution {
    static int maxEvents(int[] start, int[] end, int N) {
        // code here
         int[][] A = new int[N][2];
        
        for(int i=0; i<N; i++)
        {
            A[i][0] = start[i];
            A[i][1] = end[i];
        }
        
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        Arrays.sort(A, (a, b) -> Integer.compare(a[0], b[0]));
        int i = 0, res = 0, d = 0;
        while (!pq.isEmpty() || i < N) {
            if (pq.isEmpty())
                d = A[i][0];
            while (i < N && A[i][0] <= d)
                pq.offer(A[i++][1]);
            pq.poll();
            ++res; ++d;
            while (!pq.isEmpty() && pq.peek() < d)
                pq.poll();
        }
        return res;
    }
};