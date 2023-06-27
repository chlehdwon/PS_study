#include <cstdio>
#include <cstring>

int main(){
	int n=0, r=0;
	char str[20];
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d %s", &r, str);
		for(int j=0; j<strlen(str); j++){
			for(int k=0; k<r; k++) printf("%c", str[j]);
		}
		printf("\n");
	}
}