class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        for(int i=0;i<gcd(n,k);i++){
            int prev = i, next = (prev+k)%n;
            int temp = nums[i];
            while(next != i){
                int temp2 = nums[next];
                nums[next] = temp;
                temp = temp2;
                prev = next;
                next = (prev+k)%n;
            }
            nums[next] = temp;
        }
    }
};

/*
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
		int n=k%nums.size();
        reverse(nums.begin(),nums.end());
		reverse(nums.begin(),nums.begin()+n);
		reverse(nums.begin()+n,nums.end());
    }
};
*/


/*
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
		int 
        int n=(nums.size()-k)%nums.size();
		cout << n;
		for(int i=0; i<n; ++i)
			nums.push_back()
		for(int i=0; i<n; ++i)
			nums.erase(nums.begin());
    }
};
*/

/*
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        deque<int> d;
		for(auto ele : nums){
			d.push_back(ele);
		}
		while(k--){
			d.push_front(d.end()-1);
			d.pop_back();
		}
		for(int i=0; i<d.size(); ++i)
			nums[i]=d[i];
    }
};
*/