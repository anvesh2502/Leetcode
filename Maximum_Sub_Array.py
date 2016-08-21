public class Solution {
    public int maxSubArray(int[] nums)
    {
    int max_array_sum=0,max_ending=0;
    boolean negFlag=false;

    if(nums.length==1)
      return nums[0];


    for(int a : nums)
     {
    if(a>0)
    {
     negFlag=true;
     break;
    }
     }

     if(!negFlag)
     {
         int min=-9999;
         for(int j=0;j<nums.length;j++)
         {
             if(min<nums[j])
              min=nums[j];
         }

         return min;
     }



    for(int i=0;i<nums.length;i++)
    {
        max_ending+=nums[i];
        if(max_ending<0)
          max_ending=0;

        if(max_array_sum<max_ending)
           max_array_sum=max_ending;
    }

    return max_array_sum;
    }
}
