- #include<stdio.h>
#include <stdio_ext.h>
#include <stdlib.h>
#include <string.h>
#define MAX_GRUPO 4
    /*****Estrutura***********/
    struct selecao
{
    char time[100];
    int pontos;
    int gols;
    int gols_total;
    int gols_saldo;
};
struct selecao grupo_a[4]; // grupo A montado
/***************************/
int main()
{
    /*****Arvuivo*******/
    const char GRUPO_A[] = "/home/victor/Desktop/grupo_a.txt";
    FILE *fp;
    /*******************/
    char jogo_copa[64][200]; // total de jogos da copa - 64 jogos com tamanho de 200 caracteres por
    jogo int i = 0, j = 1, h = 0;
    char entrada[30];
    int n_temp = 0;
    int grupo_a_primeiro = 0, indice_primeiro = 0, indice_segundo = 0, grupo_a_segundo = 0;
    /********************/
    printf("PROGRAMA COPA DO MUNDO 2010.\n");
    fp = fopen(GRUPO_A, "r");
    if (fp == NULL)
        exit(1);
    printf("Digite o nome da seleção pertencente ao GRUPO A.\n");
    for (i = 0; i < MAX_GRUPO; i++)
    { // GRUPO A
        n_temp = fgets(entrada, sizeof(entrada), fp);
        // entrada[strlen(entrada)-1] = ''; // só pra tirar a quebra de linha da string
        if (n_temp == EOF)
        {
            break;

            // Atividade Reflexiva
        }
        entrada[strlen(entrada) - 1] = '';
        strcpy(grupo_a[i].time, entrada);
        // n_selecao += n_temp;
    }
    printf("\n\n");
    /*jogos do grupo A*/    /************MONTA A GRADE DE JOGOS DO GRUPO
      A*******************/
    for (h = 0; h < 6; h++) // cada grupo tem 6 jogos
    {
        for (i = 0; i < 3; i++) // quantidade de jogos de modo que não repita
        {
            for (j = i + 1; j < 4; j++) // quantidade de adversários
            {
                strcpy(jogo_copa[h], grupo_a[i].time);
                if (strcmp(jogo_copa[h], grupo_a[j].time) != 0) // faz com que um time não jogue contra ele
                    mesmo
                    {
                        strcat(jogo_copa[h], " vs ");
                        strcat(jogo_copa[h], grupo_a[j].time);
                        printf("jogo[%d] = %s\n", h, jogo_copa[h]);
                        h++;
                    }
            }
        }
    }
    /***********ENCERRA A GRADE DE JOGOS DO GRUPO
   A**************************/
    /**********INICIA A MONTAGEM DOS
   PLACARES***************************/
    printf("\n\tPLACAR DOS JOGOS:\n");
    for (h = 0; h < 6; h++)
    {
        for (i = 0; i < 3; i++)
        {
            for (j = i + 1; j < 4; j++)
            {
                printf("\n%s\n\n", jogo_copa[h]);
                printf("Digite o placar do jogo no formato: 0 x 0\n");
                fgets(entrada, sizeof(entrada), stdin);
                sscanf(entrada, "%d x %d", &grupo_a[i].gols, &grupo_a[j].gols);
                grupo_a[i].gols_total += grupo_a[i].gols;
                grupo_a[j].gols_total += grupo_a[j].gols;
                if (grupo_a[i].gols > grupo_a[j].gols)
                {
                    grupo_a[i].gols_saldo += (grupo_a[i].gols - grupo_a[j].gols);
                    grupo_a[j].gols_saldo += (grupo_a[j].gols - grupo_a[i].gols);
                    grupo_a[i].pontos += 3; /****VITÓRIA****/
                    Atividade Reflexiva
                        grupo_a[j]
                            .pontos += 0;
                }
                else if (grupo_a[i].gols == grupo_a[j].gols)
                {
                    grupo_a[i].pontos += 1;
                    grupo_a[j].pontos += 1; /****EMPATE****/
                }
                else if (grupo_a[j].gols > grupo_a[i].gols)
                {
                    grupo_a[j].gols_saldo += (grupo_a[j].gols - grupo_a[i].gols);
                    grupo_a[i].gols_saldo += (grupo_a[i].gols - grupo_a[j].gols);
                    grupo_a[j].pontos += 3;
                    grupo_a[i].pontos += 0; /***DERROTA****/
                }
                h++;
            }
        }
    }
    /************TERMINA A MONTAGEM DOS PLACARES*****************/
    /************IMPRIME A TABELA DE PONTOS**********************/
    printf("\n\n\tCLASSIFICAÇÃO DO GRUPO A: \n");
    for (i = 0; i < 4; i++)
    {
        printf("\n%s tem %d pontos.\n", grupo_a[i].time, grupo_a[i].pontos);
    }
    /*************************************************************/
    /********GOLS PRÓ**************/
    printf("\n\n\tGols PRÓ GRUPO A: \n");
    for (i = 0; i < 4; i++)
    {
        printf("\n%s tem %d gols\n", grupo_a[i].time, grupo_a[i].gols_total);
    }
    /********FIM GOLS PRÓ*********************/
    /******* SALDO DE GOLS***************/
    printf("\n\n\tSALDO DE GOLS GRUPO A: \n");
    for (i = 0; i < 4; i++)
    {
        printf("\n%s tem %d gols de saldo\n", grupo_a[i].time, grupo_a[i].gols_saldo);
    }
    /******FIM SALDO DE GOLS************/
    /*****PRIMEIRO E SEGUNDO DO GRUPO******/
    /**PRIMEIRO**/
    for (i = 0; i < 4; i++)
    {
        if (grupo_a[i].pontos > grupo_a_primeiro)
        {
            grupo_a_primeiro = grupo_a[i].pontos;
            indice_primeiro = i;
            Atividade Reflexiva
        }
    }
    /**SEGUNDO**/
    for (h = 0; h < 4; h++)
    {
        if (grupo_a[indice_primeiro].pontos > grupo_a[h].pontos)
        {
            segundo_temp = grupo_a[h].pontos; // essa parte do código está errada, só está
            aqui pra encher linguiça mesmo
                indice_segundo = h;
        }
    }
    printf("\nO PRIMEIRO COLOCADO DO GRUPO A É %s.\n", grupo_a[indice_primeiro].time);
    printf("\nO SEGUNDO COLOCADO DO GRUPO A É %s.\n", grupo_a[indice_segundo].time);
    return 0;
}
