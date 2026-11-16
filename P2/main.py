"""Aplicação de terminal para cadastro e avaliação de IMC."""

from math import isfinite

from paciente import Paciente


class SistemaIMC:
    """Coordena a entrada de dados e a exibição do resultado."""

    @staticmethod
    def ler_nome() -> str:
        while True:
            nome = input("Digite seu nome: ").strip()
            if nome:
                return nome
            print("Nome inválido. Tente novamente.")

    @staticmethod
    def ler_idade() -> int:
        while True:
            try:
                idade = int(input("Digite sua idade: ").strip())
                if idade >= 0:
                    return idade
            except ValueError:
                pass
            print("Idade inválida. Digite um número inteiro não negativo.")

    @staticmethod
    def ler_decimal(mensagem: str) -> float:
        while True:
            try:
                texto = input(mensagem).strip().replace(",", ".")
                numero = float(texto)
                if isfinite(numero) and numero > 0:
                    return numero
            except ValueError:
                pass
            print("Valor inválido. Digite um número maior que zero.")

    def executar(self) -> None:
        """Solicita os dados, cria um paciente e mostra seu relatório."""
        print("=== Cadastro de paciente e cálculo de IMC ===")
        nome = self.ler_nome()
        idade = self.ler_idade()
        peso = self.ler_decimal("Digite seu peso (kg): ")
        altura = self.ler_decimal("Digite sua altura (m): ")

        paciente = Paciente(nome, idade, peso, altura)
        print("\n=== Cadastro ===")
        print(paciente.gerar_relatorio())


def main() -> None:
    sistema = SistemaIMC()
    sistema.executar()


if __name__ == "__main__":
    main()
