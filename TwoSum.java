// O(n)
// Use a hashmap to check if corresponding counterpart is present
import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
       int[] ans = new int[2];
        HashMap<Integer, Integer> table = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            table.put(nums[i], i);
            int required = target - nums[i];
            if (table.containsKey(required)) {
               ans[0] = i;
               ans[1] = table.get(required);
            }
        }
        return ans;
    }
}

//iterate once to see if there are duplicates
//O(n^2) solution
/*
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    int[] ans = {i, j};
                    return ans;
                }
            }
        }
        int[] na = {0};
        return na;
    }
}
*/
