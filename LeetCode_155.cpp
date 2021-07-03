class MinStack {
public:
    /** initialize your data structure here. */
	stack<pair<int,int>> q;
    MinStack() {
		
    }
    
    void push(int val) {
        if(q.empty())
			q.push(make_pair(val,val));
		else{
			int min_now = min(q.top().second,val);
			q.push(make_pair(val,min_now));
		}
    }
    
    void pop() {
        q.pop();
    }
    
    int top() {
        return q.top().first;
    }
    
    int getMin() {
        return q.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */