#include<cstdio>

char word[1000001];
int alphabet[123];

int main() {
	fread(word, 1, 1000001, stdin);
	for (int i = 0; word[i]; ++i) {
		alphabet[word[i]]++;
	}
	int m = 0; char a;
	for (int i = 65; i < 91; ++i) {
		alphabet[i] += alphabet[i + 32];
		if (m < alphabet[i]) {
			m = alphabet[i];
			a = i;
		}
	}
	for (int i = 65; i < 91; ++i) {
		if (alphabet[i] == m && a != i) {
			printf("?");
			return 0;
		}
	}
	printf("%c", a);
	return 0;
}