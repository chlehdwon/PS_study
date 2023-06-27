class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
		for(auto ele : nums){
			if(set.find(ele)!=set.end())
				return true;
			set.insert(ele);
		}
		
		return false;
    }
};

/*
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
    	sort(nums.begin(),nums.end());
		for(int i=1; i<nums.size(); ++i)
			if(nums[i-1]==nums[i]) return true;
		
		return false;
    }
};
*/