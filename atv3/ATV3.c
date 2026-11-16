#include <stdio.h>
#include <string.h>

#define MAX 20

/* Estrutura da disciplina */
typedef struct {
    char nome[50];
    float nota1;
    float nota2;
    float media;
    int aproveitavel;
} Disciplina;


/* funcao para media */
float media(float x, float y)
{
    return (x + y) / 2;
}


/* funcao pra checar ser aproveita */
int aproveitaDoutorado(char nome[])
{
    if (strcmp(nome, "Calculo I") == 0 ||
        strcmp(nome, "Calculo II") == 0 ||
        strcmp(nome, "Calculo III") == 0 ||
        strcmp(nome, "FVV") == 0)
    {
        return 1;   // se aproveita
    }

    return 0;       // se não aproveita
}


/* funcao para classificacao */
void classificacao(float media)
{
    if (media >= 7)
        printf("Classificacao: Aprovado\n");
    else
        printf("Classificacao: Reprovado\n");
}


/* 3 funcao principal */
int main()
{
    Disciplina disciplinas[MAX];
    int quantidade;
    int i;

    printf("=====================================\n");
    printf(" CHECAGEM DE DISCIPLINAS PARA DOUTORADO\n");
    printf("=====================================\n");

    printf("Quantas disciplinas foram cursadas: ");
    scanf("%d", &quantidade);

    /* entrada */
    for (i = 0; i < quantidade; i++)
    {
        printf("\nDisciplina %d\n", i + 1);

        printf("nome da disciplina: ");
        scanf(" %[^\n]", disciplinas[i].nome);

        printf("digite a nota 1: ");
        scanf("%f", &disciplinas[i].nota1);

        printf("digite a nota 2: ");
        scanf("%f", &disciplinas[i].nota2);

        /* media */
        disciplinas[i].media =
            media(disciplinas[i].nota1,
                  disciplinas[i].nota2);

        /* checar aproveitamento */
        disciplinas[i].aproveitavel =
            aproveitaDoutorado(disciplinas[i].nome);
    }


    /* saida com os resultados */
    printf("\n\n=====================================\n");
    printf(" RESULTADO\n");
    printf("=====================================\n");

    for (i = 0; i < quantidade; i++)
    {
        printf("\nDisciplina: %s\n",
               disciplinas[i].nome);

        printf("Media: %.2f\n",
               disciplinas[i].media);

        classificacao(disciplinas[i].media);

        if (disciplinas[i].aproveitavel)
            printf("Aproveitavel para doutorado: SIM\n");
        else
            printf("Aproveitavel para doutorado: NAO\n");
    }

    return 0;
}
