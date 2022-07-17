// recursion with helper function 
// helper function to store max, min for each layer
// T(n) = O(1) + 2T(n/2)
// O(n)
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
 }
 
class Solution {
    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }
    public boolean helper(TreeNode x, Integer min, Integer max) {
        if (x == null) {
            return true;
        }
        if ((max != null && x.val >= max) || (min != null && x.val <= min)) {
            return false;
        }
        return helper(x.left, min, x.val) && helper(x.right, x.val, max);
    }
}