#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXN 1000000

/* ---- Lista com vetor ---- */
typedef struct { int *v; int tam; } ListaVet;

void insereInicioVet(ListaVet *l, int x) {
    memmove(l->v + 1, l->v, l->tam * sizeof(int));   // desloca tudo: O(n)
    l->v[0] = x;
    l->tam++;
}
void retiraInicioVet(ListaVet *l) {
    memmove(l->v, l->v + 1, (l->tam - 1) * sizeof(int));  // O(n)
    l->tam--;
}

/* ---- Lista com ponteiros (célula cabeça) ---- */
typedef struct Celula { int valor; struct Celula *prox; } Celula;
typedef struct { Celula *cabeca; } ListaPtr;

void insereInicioPtr(ListaPtr *l, int x) {           // O(1)
    Celula *n = malloc(sizeof(Celula));
    n->valor = x;
    n->prox = l->cabeca->prox;
    l->cabeca->prox = n;
}
void retiraInicioPtr(ListaPtr *l) {                  // O(1)
    Celula *p = l->cabeca->prox;
    l->cabeca->prox = p->prox;
    free(p);
}

int main() {
    int tamanhos[] = {10, 100, 1000, 10000, 100000, 1000000};
    printf("n;vetor_ms;ponteiros_ms\n");
    for (int t = 0; t < 6; t++) {
        int n = tamanhos[t];

        ListaVet lv; lv.v = malloc(MAXN * sizeof(int)); lv.tam = 0;
        clock_t ini = clock();
        for (int i = 0; i < n; i++) insereInicioVet(&lv, i);
        for (int i = 0; i < n; i++) retiraInicioVet(&lv);
        double tv = (double)(clock() - ini) * 1000.0 / CLOCKS_PER_SEC;
        free(lv.v);

        ListaPtr lp; lp.cabeca = malloc(sizeof(Celula)); lp.cabeca->prox = NULL;
        ini = clock();
        for (int i = 0; i < n; i++) insereInicioPtr(&lp, i);
        for (int i = 0; i < n; i++) retiraInicioPtr(&lp);
        double tp = (double)(clock() - ini) * 1000.0 / CLOCKS_PER_SEC;
        free(lp.cabeca);

        printf("%d;%.3f;%.3f\n", n, tv, tp);
        fflush(stdout);
    }
    return 0;
}
