class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
		for(string ele : tokens){
			if(ele=="+" || ele=="-" || ele=="*" || ele=="/"){
				int a = s.top();
				s.pop();
				int b = s.top();
				s.pop();
				if(ele=="+") s.push(a+b);
				else if(ele=="-") s.push(b-a);
				else if(ele=="*") s.push(b*a);
				else s.push(b/a);
			}
			else
				s.push(stoi(ele));
		}
		
		return s.top();
    }
};

