#include <stdio.h>

int main()
{
    int soma;
    int numeros [] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    float media;

    /*
    printf("Digite 10 números:");
    for (int i=0; i<10; i=i+1) {
        scanf("%d", &numeros [i]);
        // printf("i: %d\n", i);
    }
    */

    soma = 0;
    for (int i=0; i<10; i=i+1) {
        soma = soma + numeros [i];
    }

    media = soma / 10.0;

    printf("Soma: %d    Media: %f\n", soma, media);

    return 0;
}