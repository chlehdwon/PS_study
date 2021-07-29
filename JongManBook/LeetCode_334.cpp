class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int a=INT_MAX,b=INT_MAX;
		for(int i=0; i<nums.size(); ++i){
			if(ele<=a)
				a=ele;
			else if(ele<=b)
				b=ele;
			else
				return true;
		}
		
		return false;
    }
};