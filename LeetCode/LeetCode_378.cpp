// Time complexity : O(NlongN)
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int lo = matrix[0][0], hi = matrix[n-1][n-1] + 1, mid, count, tmp;
        
        while (lo < hi) {
            mid = lo + (hi - lo) / 2, tmp = n - 1, count = 0;
            
			// For each row, we count the elements that are smaller then mid
            for (int i = 0; i < n; i++) {
                while (tmp >= 0 && matrix[i][tmp] > mid) tmp--;
                count += tmp + 1;
            }
            
            if (count < k) lo = mid + 1;
            else hi = mid;
        }
        
        return lo;
    }
};


/*
Time Complexity : O(NlongN)

class Solution {
public:
    int kthSmallest(vector<vector<int>>& mat, int k) {
        priority_queue<pair<int,pair<int,int>>, vector<pair<int,pair<int,int>>> , greater<pair<int,pair<int,int>>> > pq;
        int n=mat.size();
        for(int i=0; i<n; ++i)
            pq.push({mat[0][i],{0,i}});
        
        int ans;
        while(k--)
        {
            int val=pq.top().first;
            int row=pq.top().second.first;
            int col=pq.top().second.second;
            pq.pop();
            ans=val;
            if(row!=n-1)
                pq.push({mat[row+1][col],{row+1,col}});
        }
        return ans;
    }
};
*/


/*
Time Complexity : O(N^2logN^2)

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
		priority_queue<int> pq;
		for(int y=0; y<n; ++y){
			for(int x=0; x<n; ++x){
				pq.push(matrix[y][x]);
				if(pq.size()>k) pq.pop();
			}
		}
		return pq.top();
    }
};
*/