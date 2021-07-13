class Solution {
public:
    int calculate(string s) {
		queue<char> calc;    
		auto itr = s.begin();
		while(itr!=s.end()){
			if(*itr==' ')
				++itr;
			else if(*itr=='*'){
				
			}
			else if(*itr=='/'){
				
			}
			else{
				calc.push_back(*itr);
				**itr;
			}
		}
		while(!queue.empty()){
			
		}
    }
};