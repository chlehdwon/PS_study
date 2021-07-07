#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;
class LRUCache {
public:
	unordered_map<int,int>m,cnt;
	queue<int> q;
	int n;
	
    LRUCache(int capacity) : n(capacity) { }
    
    int get(int key) {
        if(cnt.find(key)==cnt.end())
			return -1;
		q.push(key);
		cnt[key]++;
		return m[key];
    }
    
    void put(int key, int value) {
        q.push(key);
		cnt[key]++;
		m[key]=value;
		while(cnt.size()>n){
			int cur = q.front();
			q.pop();
			if(cnt[cur]--==1)
				cnt.erase(cur);
		}
    }
};

/*
using key = int;

struct Entry {
    int value;
    list<key>::iterator itr;
};

class LRUCache {
    unordered_map<key, Entry> _cache;
    //old keys move to back, new ones enter at front
    list<key> _age;
    int _capacity;
public:
    LRUCache(int capacity) {
        _capacity = capacity;
    }

    int get(int key) {
        //if key is present, renew its age and return value
        if (_cache.count(key)) {
            _age.erase(_cache[key].itr);
            _age.push_front(key);
            _cache[key].itr = _age.begin();
            return _cache[key].value;
        }
        return -1;
    }

    void put(int key, int value) {
        //if key is not present, check if the old entry need to be erased
        if (!_cache.count(key)) {
            if (_cache.size() == _capacity) {
                _cache.erase(_age.back());
                _age.pop_back();
            }
        }
        //key is present, just renew the age
        else {
            _age.erase(_cache[key].itr);
        }
        _age.push_front(key);
        _cache[key] = { value, _age.begin() };
    }
};
*/