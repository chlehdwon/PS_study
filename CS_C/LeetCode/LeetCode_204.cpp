class Solution {
public:
    int countPrimes(int n){
		if(n<=2) return 0;
		vector<bool> nums(n,true);
		nums[0]=false; nums[1]=false;
		ans=0;
		for(int i=2; i*i<n; ++i){
			if(nums[i]==false) continue;
			ans++;
			for(int j=i*i; j<n; j+=i)
				nums[j]=false;
		}
		return ans;
    }
};