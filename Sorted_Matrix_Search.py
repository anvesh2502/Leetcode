public class Solution {
    public boolean searchMatrix(int[][] a, int target)
    {

     int r=0;
     int c=a[0].length-1;

     while(r<a.length && c>=0)
     {
         if(a[r][c]==target)
          return true;

         if(a[r][c]>target)
         {
             c--;
             continue;
         }

         if(a[r][c]<target)
         {
             r++;
             continue;
         }



     }
     return false;






    }
}
