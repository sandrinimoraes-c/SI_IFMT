#include <stdio.h>

int ehPrimo(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int N, contador = 0, num = 2;

    printf("Digite N: ");
    scanf("%d", &N);

    printf("Primeiros %d numeros primos: ", N);
    while (contador < N) {
        if (ehPrimo(num)) {
            printf("%d ", num);
            contador++;
        }
        num++;
    }
    printf("\n");
    return 0;
}

//Complexidade: O(N · √M), onde M é o valor do N-ésimo primo — para cada candidato testado (até √num) verifica-se a primalidade.