#include <cstdio>
#include <cstring>

int main(){
	char quiz[81];
	int n=0, w=1, score=0;
	scanf("%d", &n);
	getchar();
	for(int i=0; i<n; i++){
		fgets(quiz, 81, stdin);
		score=0;
		for(int j=0; j<strlen(quiz); j++){
			if(quiz[j]=='O') score+=w++;
			else w=1;
		}
		
		printf("%d\n", score);
	}
	
	return 0;
}

/*
#include <cstdio>

int t;
char s[81];

int main(){
	
    scanf("%d", &t);
	
	while(t--){
		int cnt = 0, ans = 0;
        scanf("%s", s);
        for(int i = 0; s[i]; ++i){
			s[i] == 'O' ? ans += ++cnt : cnt = 0; 
		}
        printf("%d\n", ans);
    }
	
	return 0;
}
*/