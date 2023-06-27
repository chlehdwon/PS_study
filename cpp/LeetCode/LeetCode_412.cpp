class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ans;
		for(int i=1; i<=n; ++i){
			bool fizz = i%3;
			bool buzz = i%5;
			if(fizz && buzz)
				ans.push_back(to_string(i));
			else if(fizz && !buzz)
				ans.push_back("Buzz");
			else if(!fizz && buzz)
				ans.push_back("Fizz");
			else
				ans.push_back("FizzBuzz");
		}
		
		return ans;
    }
};