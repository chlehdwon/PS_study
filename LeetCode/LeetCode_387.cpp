class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> v(26,0);
		for(char c : s) v[c - 'a']++;
		for(int i = 0; i < s.length(); i++){
			if(v[s[i] - 'a'] == 1) return i;
		}
		return -1;
    }
};


/*
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,pair<int,int>> set;
		int min_pos = s.size();
		for(int i=0; i<s.size(); ++i){
			if(set.find(s[i])==set.end())
				set.insert(make_pair(s[i],make_pair(1,i)));
			else
				set[s[i]].first+=1;
		}
		for(auto p : set){
			if(p.second.first==1)
				min_pos = min(min_pos,p.second.second);
		}
		
		return min_pos == s.size() ? -1 : min_pos;
    }
};
*/