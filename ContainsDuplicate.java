//add items into a hashset and see if they are added
//O(n) solution
import java.util.HashSet;
import java.util.Set;
class Solution {
  public boolean containsDuplicate(int[] nums) {
    Set a  = new HashSet<Integer>();
    for (int i = 0; i < nums.length; i++) {
      if (!a.add(nums[i])) {
        return true;
      }
    }
    return false;
  }
}
