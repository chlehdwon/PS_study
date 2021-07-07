class Solution {
public:
    int titleToNumber(string columnTitle) {
        int size=columnTitle.size(),temp=1,ans=columnTitle[size-1]-'A'+1;
        for(int i=columnTitle.size()-2; i>=0; --i){
            temp*=26;
            ans+=temp*(columnTitle[i]-'A'+1);
        }
        
        return ans;
    }
};

/*
class Solution {
public:
    int titleToNumber(string columnTitle) 
    {
        int res = 0;
        int n = columnTitle.size();
        for(int i = 0; i < n; i++)
            res = res * 26 + (columnTitle[i] - 'A' + 1);
    
        return res;
        
    }
};
*/