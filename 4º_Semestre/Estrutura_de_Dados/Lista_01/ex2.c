#include <stdio.h>

int main() {
    int n = 10, num, maior, menor;

    printf("Digite o numero 1: ");
    scanf("%d", &num);
    maior = menor = num;

    for (int i = 1; i < n; i++) {
        printf("Digite o numero %d: ", i + 1);
        scanf("%d", &num);
        if (num > maior) maior = num;
        if (num < menor) menor = num;
    }

    printf("Maior: %d\n", maior);
    printf("Menor: %d\n", menor);
    return 0;
}

//Complexidade: O(n) — cada número é comparado uma única vez.