#define MAX 100001

class Solution {
public:
	int[10001] cache;
    int numSquares(int n) {
        memset(cache,-1,sizeof(cache));
		return dp(n);
    }
	
	int dp(int n){
		if(n==1) return 1;
		if(n==0) return 0;
		int& ret = cache[n];
		if(ret!=-1) return ret;
		ret=MAX;
		for(int i=1; i*i<=n; ++i)
			ret = min(ret, 1+dp(n-i*i));
		return ret;
	}
	
};