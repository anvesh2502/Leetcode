/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {

    ArrayList<Integer> sum=new ArrayList<Integer>();

    public int sumNumbers(TreeNode root)
    {
    int s=0;
    if(root==null)
    return 0;
    if(root.left!=null)
    sumNumbers(root.left,""+root.val);
    if(root.right!=null)
    sumNumbers(root.right,""+root.val);
    if(root.left==null && root.right==null)
    return root.val;
    for(Integer v : sum)
    s+=v;
    return s;
    }

    public void sumNumbers(TreeNode root,String num)
    {
        if(root.left==null && root.right==null)
           {
               num=num+""+root.val;
               int res=Integer.parseInt(num);
               sum.add(res);
           }

        if(root.left!=null)
          sumNumbers(root.left,num+""+root.val);

        if(root.right!=null)
         sumNumbers(root.right,num+""+root.val);


    }

}
