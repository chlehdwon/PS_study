#include <cstdio>
#include <cmath>

int main(){
	int n, tmp;
	long long int length = 0;
	int scale = 0;
	
	scanf("%d", &n);
	tmp=n;
	// get scale by using while loop
	while(tmp){
		scale++;
		tmp/=10;
	}
	// sum the total length of nums which have same length as n
	length += (n-pow(10,scale-1)+1)*scale;
	// sum the total length of shorter nums than n
	for(int i=1; i<scale; i++){
		length += (pow(10, i)-pow(10, i-1))*i;
	}
	
	printf("%lld\n", length);

	return 0;
}

/*
#include<cstdio>
int n, r;
int main() {
    scanf("%d", &n);
	// very fast
    for (int i = 1; i <= n; i *= 10) 
		r += n - i + 1;
    printf("%d", r);
    return 0;
}
*/