/* 이상한 scanf */
#include <stdio.h>
#include <string.h>

int main(void)
{
    //getchar. ---------------
    printf("[input] : ");
    int arr[10];
    for (int i = 0; i < 10; ++i)
    {
        arr[i] = getchar();    //열개의 char를 받습니다. 
    }
	return 0;
}