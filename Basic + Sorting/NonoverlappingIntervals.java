import java.util.Arrays;
// sort by start
// sort then iterate O(nlogn)
class Solution {
    public static int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (x, y) -> x[0] - y[0]);
        int toRemove = 0;
        int ending = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            // overlapping 
            if (intervals[i][0] < ending) {
                //take the one that ends earlier
                if (intervals[i][1] <= ending) {
                    ending = intervals[i][1];
                } 
                toRemove ++;
            } else {
                //if not overlap, take the one that ends later
                if (intervals[i][1] > ending) {
                    ending = intervals[i][1];
                } 
            }
        }
        return toRemove;
    }

    public static void main(String args[]) {
        int[][] intervals = {{1,2},{2,3},{3,4},{1,3}};
        System.out.println(eraseOverlapIntervals(intervals));
        // return 1
    }
}

