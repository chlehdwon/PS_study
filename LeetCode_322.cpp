#define MAX 987654321
class Solution {
public:
	int cache[10001];
    int coinChange(vector<int>& coins, int amount) {
        memset(cache,0,sizeof(cache));
		sort(coins.begin(),coins.end());
		int ans = dp(coins,amount);
		return ans!=MAX ? ans : -1;
    }
	
	int dp(vector<int>& coins, int amount){
		if(amount==0) return 0;
		int& ret = cache[amount];
		if(ret!=0) return ret;
		ret = MAX;
		for(int i=coins.size()-1; i>=0; --i)
			if(coins[i]<=amount)
				ret=min(ret,1+dp(coins,amount-coins[i]));
		
		return ret;
	}
};