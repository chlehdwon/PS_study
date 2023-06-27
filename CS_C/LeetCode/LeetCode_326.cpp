class Solution {
public:
    bool isPowerOfThree(int n) {
		return n > 0 && 1162261467 % n == 0;
    }
};

/*
class Solution {
public:
    bool isPowerOfThree(int n) {
		if(n==0) return false;
        if(n==1) return true;
		if(n%3!=0) return false;
		return isPowerOfThree(n/3);
    }
};
*/