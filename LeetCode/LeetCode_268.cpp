class Solution {
public:
    int missingNumber(vector<int>& nums) {
		int miss = nums.size();
		for(int i=0; i<nums.size(); ++i){
			miss^=i^nums[i];
		}
		
		return miss;
    }
};

/*
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = nums.size() * (nums.size()+1) / 2;
		for(int ele : nums)
			sum-=ele;
		return sum;
    }
};
*/