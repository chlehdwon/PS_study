/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
	* class NestedInteger {
	*   public:
	*     // Return true if this NestedInteger holds a single integer, rather than a nested list.
	*     bool isInteger() const;
	*
	*     // Return the single integer that this NestedInteger holds, if it holds a single integer
	*     // The result is undefined if this NestedInteger holds a nested list
	*     int getInteger() const;
	*
	*     // Return the nested list that this NestedInteger holds, if it holds a nested list
	*     // The result is undefined if this NestedInteger holds a single integer
	*     const vector<NestedInteger> &getList() const;
	* };
 */

queue<int> qIntegers;
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (auto& niIt : nestedList) {
            if (niIt.isInteger()) 
                qIntegers.push(niIt.getInteger());
            else
                NestedIterator(niIt.getList());
        }
    }
    
    int next() {
        int nextInt = qIntegers.front();
        qIntegers.pop();
        return nextInt;
    }
    
    bool hasNext() {
        return !qIntegers.empty();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */