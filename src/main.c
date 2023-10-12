#include <stdio.h>
#include <stdlib.h>

int main()
{

    int n;
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        for(int k=n-i-1;k>0;k--)
            printf(" ");
        for(int k=0;k<(i+1)*2-1;k++)
                printf("*");
        printf("\n");
    }
    for (int i=0;i<n;i++){
        for(int k=0;k<(i+1);k++)
            printf(" ");
        for(int k=n*2-(i+1)*2-1;k>0;k--)
            printf("*");
        printf("\n");


    }
    printf("완료");
    return 0;
}
