class Solution {
public:
	void moveZeroes(vector<int>& nums) {
		int lastNonZeroFoundAt = 0;
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] != 0) {
				nums[lastNonZeroFoundAt++] = nums[i];
			}
		}
		for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
			nums[i] = 0;
		}
	}
	
	/*
    void moveZeroes(vector<int>& nums) {
        int z=0, nz=0, len=nums.size();
		while(z<len && nums[z]!=0){z++;}
		nz=z;
		while(nz<len){
			while(z<len && nums[z]!=0){z++;}
			while(nz<len && nums[nz]==0){nz++;}
			if(nz>=len || z>=len)
				break;
			swap(nums[nz],nums[z]);
		}
		return;
    }
	*/
};