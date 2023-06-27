/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<TreeNode*> nodes;
	
    int kthSmallest(TreeNode* root, int k) {
		return nodes[k-1];
    }
	
	void inorder(TreeNode* root){
		if(root==nullprt) return;
		inorder(root->left);
		nodes.push_back(root);
		inorder(root->right);
		return;
	}
};

/*
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        TreeNode* cur=root;
        stack<TreeNode*>s;
       while(cur!=NULL || s.empty()==false)
       {
           while(cur!=NULL)
           {
               s.push(cur);
               cur=cur->left;
           }
           cur=s.top()->right;
           k--;
           if(k==0)
               return s.top()->val;
           s.pop();
       }
       return 0;
    }
};
*/
    