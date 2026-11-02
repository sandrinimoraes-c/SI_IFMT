#include <stdio.h>
#include <stdlib.h>

struct Celula {
    int valor;
    struct Celula *prox;
};

struct Lista {
    struct Celula *primeira;
    struct Celula *ultima;
};

void inicializarLista(struct Lista *lista) {
    lista->primeira = malloc(sizeof(struct Celula));
    lista->ultima = lista->primeira;
    lista->ultima->prox = NULL;
}

void inserir(struct Lista *lista, int val) {
    struct Celula *novaCel = malloc(sizeof(struct Celula));
    lista->ultima->prox = novaCel;
    lista->ultima = novaCel;
    novaCel->valor = val;
    novaCel->prox = NULL;
}

void imprimir(struct Lista *lista) {
    struct Celula *celAtual = lista->primeira->prox;
    printf("[");
    while (celAtual != NULL) {
        printf("%d, ", celAtual->valor);
        celAtual = celAtual->prox;
    }
    printf("]\n");
}

void remover(struct Lista *lista, int index) {
    struct Celula *celAtual = lista->primeira->prox;
    struct Celula *celAnterior = lista->primeira;
    int i = 0;

    while (i < index && celAtual != NULL) {
        celAnterior = celAtual;
        celAtual = celAtual->prox;
        i++;
    }

    if (celAtual == NULL) {
        printf("Indice %d invalido.\n", index);
        return;
    }

    celAnterior->prox = celAtual->prox;

    if (celAtual == lista->ultima) {
        lista->ultima = celAnterior;
    }

    free(celAtual);
}

void liberarLista(struct Lista *lista) {
    struct Celula *celAtual = lista->primeira;
    while (celAtual != NULL) {
        struct Celula *prox = celAtual->prox;
        free(celAtual);
        celAtual = prox;
    }
    lista->primeira = NULL;
    lista->ultima = NULL;
}

int main() {
    struct Lista lista1;
    inicializarLista(&lista1);

    inserir(&lista1, 5);
    inserir(&lista1, 9);
    inserir(&lista1, 11);
    inserir(&lista1, 19);
    imprimir(&lista1);

    remover(&lista1, 1);
    imprimir(&lista1);

    remover(&lista1, 0);
    imprimir(&lista1);

    liberarLista(&lista1);
    return 0;
}