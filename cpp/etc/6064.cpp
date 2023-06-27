#include <cstdio>
#include <cmath>

int getyears(int m, int n, int x, int y);
int getgcd(int a, int b);

int main(int argc, const char * argv[]){
	int n;
	int arr[1000][4];
	scanf("%d", &n);
	// get inputs
	for(int i=0; i<n; i++){
		scanf("%d %d %d %d", &arr[i][0], &arr[i][1], &arr[i][2], &arr[i][3]);
	}
	// print answers
	for(int i=0; i<n; i++){
			printf("%d\n", getyears(arr[i][0], arr[i][1], arr[i][2], arr[i][3]));
	}
		
	return 0;
}

int getyears(int m, int n, int x, int y){
	int years = 0;
	int gcd = getgcd(m,n);
	// calculate lcd because lcd is the max number of years
	int lcm = m*n/gcd;
	// focus at bigger number for less comparison
	if(m>=n){
		years=x;
		// check whether years satisfies the conditions
		while(years<=lcm){
			if(years%n==y || years%n==y-n) return years;
			else years+=m;
		}
		// it means there is no answer
		return -1;
	}
	else{
		years=y;
		while(years<=lcm){
			if(years%m==x || years%m==x-m) return years;
			else years+=n;
		}
		return -1;
	}
	
	return -1;
}

int getgcd(int a, int b) {
    while(b) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}