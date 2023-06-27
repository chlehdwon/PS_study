#include <iostream>

using namespace std;
int main(){
	int n,k;
	int num=1;
	cin>>n>>k;
	for(int i=1; i<=n; ++i){
		num*=i;
	}
	for(int i=1; i<=k; ++i){
		num/=i;
	}
	for(int i=1; i<=n-k; ++i){
		num/=i;
	}
	cout << num << endl;
	
	return 0;
}

/*
long c(int n, int r) { return r && n != r ? c(n - 1, r - 1) + c(n - 1, r) : 1; }

int main()
{
  int n, r;
  scanf("%d%d", &n, &r);
  printf("%ld", c(n, r));
}
*/