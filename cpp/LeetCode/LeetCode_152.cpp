class Solution {
public:
    int maxProduct(vector<int>& nums) 
    {
		// empty array case
		if (nums.size() == 0)
			return 0;
			
	    // maxSub and minSub will hold the products till nums[i]
        int maxSub = nums[0];   
        int minSub = nums[0];
        int maxProductSub = nums[0];
        
        for (size_t i = 1; i < nums.size(); i++)
        {
            // element is negative so we swap max and min
            // because when multiplying negative with a negative, number becomes positive so minimum negative number will become the maximum number
            if (nums[i] < 0)
                swap(minSub, maxSub);
      
            // update all the sub values
			maxSub = max(maxSub * nums[i], nums[i]); 
            minSub = min(minSub * nums[i], nums[i]); 
            // choose max product to be the max between the maxProduct till now and maxSub
			maxProductSub = max(maxProductSub, maxSub); 
        }
		
        return maxProductSub;
    }
   
};
/*
class Solution {
public:
    int maxProduct(vector<int>& nums) {
		if(nums.size()==1)
			return nums[0];
		
		int left=-1,right=-1;
		int product=1;
		vector<int> sub_prod(nums.size());
       	for(int i=0; i<sub_prod.size(); ++i){
			if(nums[i]==0){
				product=1;
				sub_prod[i]=0;
			}
			else{
                product*=nums[i];
                sub_prod[i]=product;
			}
		}
		product=0;
		for(int i=0; i<sub_prod.size(); ++i){
			if(sub_prod[i]==0){
				if(left!=-1 && right!=left)
					product=max(product,sub_prod[right]/sub_prod[left]);
				right=left=-1;
			}
			else if(sub_prod[i]<0){
				if(left==-1) right=left=i;
				else right=i;
			}
			else
				product=max(product,sub_prod[i]);
		}
		if(left!=-1 && right!=left)
					product=max(product,sub_prod[right]/sub_prod[left]);
		
		return product;
    }
};
*/