class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()>nums2.size())
			return intersect(nums2,nums1);
		unordered_map<int,int> a,b;
		vector<int> ans;
		for(auto ele : nums1)
			a[ele]+=1;
		for(auto ele : nums2)
			b[ele]+=1;
		for(auto ele : a)
			if(b.find(ele.first))!=b.end())
				auto result = b.find(ele)
				int cnt = min(a[ele],result->second);
				while(cnt--)
					ans.push_back(result->first);
		return ans;
    }
};

/*
class Solution {// Using Map & without sort
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int,int>freq;
        vector<int>ans;
        for(int i = 0;i<nums1.size();i++){
            freq[nums1[i]]++;
        }
        for(int i = 0;i<nums2.size();i++){
            if (freq[nums2[i]] > 0){
                freq[nums2[i]]--; 
                ans.push_back(nums2[i]);
            }
        }
        return ans;
    }
};
*/
