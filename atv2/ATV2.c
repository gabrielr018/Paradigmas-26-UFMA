#include <stdio.h>
#include <stdbool.h>

int main() {
    float saldo = 0.0;
    float valor;
    int opcao;
    bool continuar = true;

    while (continuar) {

        printf("\n*** PDV CAIXA ***\n");
        printf("1 - Consultar Saldo\n");
        printf("2 - Depositar\n");
        printf("3 - Sacar\n");
        printf("4 - Encerrar\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        if (opcao == 1) {

            printf("\nSaldo Atual: R$ %.2f\n", saldo);

        } else if (opcao == 2) {

            printf("\nDigite o valor do deposito: R$ ");
            scanf("%f", &valor);

            if (valor > 0) {
                saldo = saldo + valor;

                printf("\nDeposito realizado com sucesso!\n");
                printf("===== RECIBO =====\n");
                printf("Operacao: Deposito\n");
                printf("Valor: R$ %.2f\n", valor);
                printf("==================\n");

            } else {
                printf("\nValor invalido!\n");
            }

        } else if (opcao == 3) {

            printf("\nDigite o valor do saque: R$ ");
            scanf("%f", &valor);

            if (valor > 0) {

                if (valor <= saldo) {
                    saldo = saldo - valor;

                    printf("\nSaque realizado com sucesso!\n");
                    printf("===== RECIBO =====\n");
                    printf("Operacao: Saque\n");
                    printf("Valor: R$ %.2f\n", valor);
                    printf("==================\n");

                } else {
                    printf("\nSaldo insuficiente!\n");
                }

            } else {
                printf("\nValor invalido!\n");
            }

        } else if (opcao == 4) {

            continuar = false;
            printf("\nCaixa encerrado. Obrigado!\n");

        } else {

            printf("\nOpcao invalida! Tente novamente.\n");
        }
    }

    return 0;
}
