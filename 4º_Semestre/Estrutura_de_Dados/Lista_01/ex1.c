#include <stdio.h>

int main() {
    int n = 10, num;
    float soma = 0;

    for (int i = 0; i < n; i++) {
        printf("Digite o numero %d: ", i + 1);
        scanf("%d", &num);
        soma += num;
    }

    printf("Soma: %.2f\n", soma);
    printf("Media: %.2f\n", soma / n);
    return 0;
}

// Complexidade: O(n) — um laço percorre os 10 números uma vez.