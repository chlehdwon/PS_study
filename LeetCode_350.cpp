class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()>nums2.size())
			return intersect(nums2,nums1);
		unordered_set<int> a;
		unordered_set<int> b;
		vector<int> ans;
		for(auto ele : nums1)
			a.insert(ele);
		for(auto ele : nums2)
			b.insert(ele);
		for(auto ele : a)
			if(b.find(ele)!=b.end())
				ans.push_back(ele);
		return ans;
    }
};