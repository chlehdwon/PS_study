class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> counter;
		priority_queue<pair<int,int>> pq;
		vector<int> ans;
		for(auto ele : nums)
			counter[ele]+=1;
		for(auto p : counter){
			pq.push(make_pair(-p.second, p.first));
			if(pq.size()>k) pq.pop();
		}
		for(int i=0; i<k; ++i){
			ans.push_back(pq.top().second);
			pq.pop();
		}
		return ans;
    }
};

/*
Map + BucketSort Solution O(N)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        int n = nums.size();
        if(k==n)return nums;    // base case
        
        vector<int>res;  // result vector
        
        // store number counts in Map
        unordered_map<int,int>track;    
        for(auto &t: nums)track[t]++;
        
        // add all numbers from Map in to buckets and track the max count
        int maxc =  INT_MIN;
        vector<int> bucket[n+1];
        for(auto &t: track)bucket[t.second].push_back(t.first),maxc=max(maxc,t.second);
        
        // add all items from max count bucket in to result and in descending order of count
        int curr = maxc;
        while(res.size()<k)
        {
            // It is guaranteed that the answer is unique.
            if(!bucket[curr].empty())res.insert(res.end(),bucket[curr].begin(),bucket[curr].end());
            curr--;
        }
        
        return res;
    }
};
*/