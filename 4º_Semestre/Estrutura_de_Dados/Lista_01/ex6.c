#include <stdio.h>

int main() {
    int N;
    long long a = 0, b = 1, prox;

    printf("Digite N: ");
    scanf("%d", &N);

    printf("Sequencia de Fibonacci: ");
    for (int i = 0; i < N; i++) {
        if (i == 0) printf("%lld ", a);
        else if (i == 1) printf("%lld ", b);
        else {
            prox = a + b;
            a = b;
            b = prox;
            printf("%lld ", prox);
        }
    }
    printf("\n");
    return 0;
}

//Complexidade: O(n) — cada termo é calculado em tempo constante a partir dos dois anteriores.