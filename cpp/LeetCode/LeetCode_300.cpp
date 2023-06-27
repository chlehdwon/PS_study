class Solution {
public:
    int lengthOfLIS(vector<int>& A) {
        int len = 0;
        for(auto cur : A) 
            if(len == 0 || A[len-1] < cur) A[len++] = cur;             // extend
            else *lower_bound(begin(A), begin(A) + len, cur) = cur;    // replace
        return len;
    }
};

/*
class Solution {
public:
	int cache[2500];
    int lengthOfLIS(vector<int>& nums) {
        memset(cache,-1,sizeof(cache));
		int ans=1;
		for(int i=0; i<nums.size(); ++i){
			ans=max(ans,dp(i,nums));
		}
		
		return ans;
    }
	
	int dp(int start, vector<int>& nums){
		int& ret = cache[start];
		if(ret!=-1) return ret;
		ret=1;
		for(int i=start+1; i<nums.size(); ++i)
			if(nums[i]>nums[start])
				ret = max(ret,1+dp(i,nums));
		return ret;
	}
};
*/