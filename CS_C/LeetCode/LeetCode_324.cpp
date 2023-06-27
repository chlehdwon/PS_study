class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int size = nums.size();
        nth_element(begin(nums), begin(nums) + size / 2, end(nums));
        int m = *(begin(nums) + size / 2);
        
        #define A(i) nums[(1 + 2*(i)) % (size | 1)]
        // size|1 means the next odd numbers when size is even.
		// ex) 110 | 1 = 111 / 111 | 1 = 111
		// so, for the numbers that less than median give odd,
		// others give even.
        int l = 0, r = size - 1;
        for (int i = 0; i <= r;)
            if (A(i) > m) swap(A(i++), A(l++));
            else if (A(i) < m) swap(A(i), A(r--));
            else i++;
    }
};