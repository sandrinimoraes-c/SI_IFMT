#include <stdio.h>
#include <stdlib.h>

void counting_sort(int v[], int n) {
    if (n <= 1) return;

    // Descobre o menor e o maior valor (permite até números negativos)
    int min = v[0], max = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < min) min = v[i];
        if (v[i] > max) max = v[i];
    }
    int k = max - min + 1;               // tamanho do intervalo

    int *count = calloc(k, sizeof(int)); // vetor de contagem (zerado)
    int *saida = malloc(n * sizeof(int));
    if (count == NULL || saida == NULL) {
        printf("Erro de alocacao de memoria\n");
        free(count);
        free(saida);
        return;
    }

    // Passo 1: contar ocorrências
    for (int i = 0; i < n; i++)
        count[v[i] - min]++;

    // Passo 2: soma acumulada
    for (int i = 1; i < k; i++)
        count[i] += count[i - 1];

    // Passo 3: montar a saída (da direita para a esquerda => estável)
    for (int i = n - 1; i >= 0; i--) {
        saida[--count[v[i] - min]] = v[i];
    }

    // Copia o resultado de volta para o vetor original
    for (int i = 0; i < n; i++)
        v[i] = saida[i];

    free(count);
    free(saida);
}

int main(void) {
    int v[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Antes:  ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);

    counting_sort(v, n);

    printf("\nDepois: ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);
    printf("\n");
    return 0;
}