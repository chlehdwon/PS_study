class Solution {
public:
    int fourSumCount(vector<int>& a, vector<int>& b, vector<int>& c, vector<int>& d) {
        // support variables
        int res = 0;
        unordered_map<int, int> abMap;
        // populating abMap as frequency tables of sums
        for (int i: a) for (int j: b) abMap[i + j]++;
        // finding if we have opposite matches in abMap and cdMap
        for (int i: c) for (int j: d) {
            // looking for the pointer to the opposite element
            auto p = abMap.find(-i - j);
            // if not we move on
            if (p == end(abMap)) continue;
            // otherwise we update res
            res += p->second;
        }
        return res;
    }
};

/*
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> sum_of_12;
		unordered_map<int, int> sum_of_34;
		int ans=0;
		int size=nums1.size();
		for(int i=0; i<size; ++i){
			for(int j=0; j<size; ++j){
				sum_of_12[nums1[i]+nums2[j]]+=1;
				sum_of_34[nums3[i]+nums4[j]]+=1;
			}
		}
		
		for(auto p : sum_of_12){
			auto itr = sum_of_34.find(-p.first);
			if(itr!=sum_of_34.end())
				ans+=(p.second*(*itr).second);
		}
		
		return ans;
    }
};
*/