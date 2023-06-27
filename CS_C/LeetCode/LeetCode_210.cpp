class Solution {
public:
	bool bfs(int n, vector<int>& ans, vector<vector<int>>& graph, vector<int>& degree){
		queue<int> q;
		for(int i=0; i<n; ++i)
			if(degree[i]==0)
				q.push(i);
		
		while(!q.empty()){
			int curr = q.front();
			q.pop();
			for(auto ele : graph[curr]){
				degree[ele]-=1;
				if(degree[ele]==0)
					q.push(ele);
			}
			ans.push_back(curr);
		}
		
		return ans.size()==n;
	}
	
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
		vector<int> ans;
		vector<vector<int>> graph(numCourses);
		vector<int> degree(numCourses,0);
		for(auto ele : prerequisites){
			graph[ele[1]].push_back(ele[0]);
			degree[ele[0]]+=1;
		}
		if(bfs(numCourses,ans,graph,degree))
			return ans;
		
		return {};
    }
};

/*
class Solution {
public:
    int color[2001] = {0};
    // 0 -> white or unvisited
    // 1 -> gray or visiting
    // 2-> black or visited
    bool DFS(int v, vector<int> adj[], vector<int>&res) {
    if(color[v]==1) { // when you meet the same node twice which traversing the route , it has a cycle
        return false; // break from cycle
    }
	color[v] = 1;

	for(int u = 0; u < adj[v].size(); ++u ) {    
    	if(color[adj[v][u]]==0) { // visit only unvisited nodes
             if(!DFS(adj[v][u], adj, res)) { // if cycle discovered , break free and return false
                 return false;
             }
		}
        if(color[adj[v][u]]==1) {
             return false;
         }
		
	}
    color[v] = 2;
    res.push_back(v);
	return true;
}    

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    int n = prerequisites.size();
	vector<int> adj[numCourses];
	vector<int> res;
	for(int i = 0; i < n; ++i) {
		adj[prerequisites[i][0]].push_back(prerequisites[i][1]);
	}
	
	for(int v = 0; v < numCourses; ++v) {
        if(color[v]==0) { 
            if (!DFS(v, adj, res))  return {}; 
        }
	}
	return res;
    }
};
*/