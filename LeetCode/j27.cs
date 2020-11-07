/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode MirrorTree(TreeNode root) {
        if(root!=null){
            MirrorTree(root.left);
            MirrorTree(root.right);
            TreeNode tmp=null;
            tmp=root.left;
            root.left=root.right;
            root.right=tmp;
        }
        return root;
    }
}