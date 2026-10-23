#include <stdio.h>
#include <string.h>
#define MAX 1000

typedef struct { char v[MAX]; int topo; } Pilha;

void empilha(Pilha *p, char c) { p->v[p->topo++] = c; }
char desempilha(Pilha *p)      { return p->v[--p->topo]; }

/* Ideia: abriu -> empilha. Fechou -> desempilha e confere se é o par correto.
   No fim a pilha precisa estar vazia. */
int bemFormada(char *s) {
    Pilha p; p.topo = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            empilha(&p, c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (p.topo == 0) return 0;                 // fechou sem abrir
            char a = desempilha(&p);
            if ((c == ')' && a != '(') || (c == ']' && a != '[') || (c == '}' && a != '{'))
                return 0;                              // par errado
        }
    }
    return p.topo == 0;                                // sobrou algo aberto?
}

int main() {
    char s[MAX];
    printf("Digite a sequencia: ");
    scanf("%s", s);
    printf(bemFormada(s) ? "Bem formada\n" : "Mal formada\n");
    return 0;
}
