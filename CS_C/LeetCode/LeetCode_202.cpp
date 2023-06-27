class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> cache;
		while(n!=1){
			int temp=0;
			while(n){
				temp+=(n%10)*(n%10);
				n/=10;
			}
			if(temp==1) return true;
			else{
				if(cache.find(temp)!=cache.end())
					return false;
				cache.insert(temp);
				n=temp;
			}
		}
		
		return true;
    }
};