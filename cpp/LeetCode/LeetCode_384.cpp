class Solution {
public:
    Solution(const vector<int>& nums) : nums(nums), arr(nums), seed(random_device{}()) {}

    vector<int> reset() {
		arr = nums;
		return arr;
	}

    vector<int> shuffle() {
        for (int i = size(arr) - 1; i > 0; --i) {
            auto idx = uniform_int_distribution<int>(0, i)(seed);
            swap(arr[i], arr[idx]);
        }
        return arr;
    }
private:
    vector<int> arr, nums;
    default_random_engine seed;
};

/*
class Solution {
	vector<int> original;
	int n;
public:

	Solution(vector<int>& nums) {
		original = nums;
		n = original.size();
	}
	
	vector<int> reset() {
		return original;
	}
	
	vector<int> shuffle() {
			//make a copy of the original
			vector<int> shuffled = original;
			
			int leftSize = n;
			for(int i = n-1; i>=0; i--) {
				//draw from the bag
				int j = rand()%leftSize;
				
				//put this element at current position
				//and put the original element in the bag
				swap(shuffled[i], shuffled[j]);
				leftSize--;
			}
			return shuffled;
	}
	
};
*/