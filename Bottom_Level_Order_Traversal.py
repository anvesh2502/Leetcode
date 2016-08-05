import java.util.*;
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

    LinkedHashMap<Integer,ArrayList<Integer>> levelMap=new LinkedHashMap<Integer,ArrayList<Integer>>();


    public List<List<Integer>> levelOrderBottom(TreeNode root)
    {
        levelOrderBottom(root,0);
        List<List<Integer>> l=new ArrayList<List<Integer>>();
        for(int i=levelMap.size()-1;i>=0;i--)
        {
            l.add(levelMap.get(i));

        }
        return l;
    }

    public void levelOrderBottom(TreeNode root,int level)
    {
        if(root==null)
        return;
        ArrayList<Integer> vals;
        if(levelMap.containsKey(level))
        {
          vals=levelMap.get(level);
        }
        else
        {
            vals=new ArrayList<Integer>();
        }
        vals.add(root.val);
        levelMap.put(level,vals);
        levelOrderBottom(root.left,level+1);
        levelOrderBottom(root.right,level+1);
    }

}
