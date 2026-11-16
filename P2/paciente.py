"""Modelo de paciente e regras de cálculo do IMC."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Paciente:
    """Representa um paciente com dados válidos para o cálculo do IMC."""

    nome: str
    idade: int
    peso: float
    altura: float

    def __post_init__(self) -> None:
        """Valida os dados ao criar um paciente."""
        if not isinstance(self.nome, str) or not self.nome.strip():
            raise ValueError("O nome não pode ficar vazio.")

        if isinstance(self.idade, bool) or not isinstance(self.idade, int) or self.idade < 0:
            raise ValueError("A idade deve ser um número inteiro não negativo.")

        if not isinstance(self.peso, (int, float)) or not isfinite(self.peso) or self.peso <= 0:
            raise ValueError("O peso deve ser um número positivo.")

        if not isinstance(self.altura, (int, float)) or not isfinite(self.altura) or self.altura <= 0:
            raise ValueError("A altura deve ser um número positivo.")

        # Ajusta espaços extras sem alterar o restante dos dados.
        object.__setattr__(self, "nome", self.nome.strip())

    def calcular_imc(self) -> float:
        """Calcula o Índice de Massa Corporal (kg/m²)."""
        return self.peso / (self.altura ** 2)

    def classificar_imc(self) -> str:
        """Retorna a faixa de IMC de acordo com as regras do exercício."""
        imc = self.calcular_imc()

        if imc < 18.5:
            return "Paciente está abaixo do peso"
        if imc < 25:
            return "Paciente está com o peso normal"
        if imc < 30:
            return "Paciente está acima do peso"
        return "Paciente está com obesidade"

    def gerar_relatorio(self) -> str:
        """Organiza os dados e o resultado em formato de texto."""
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Peso: {self.peso:g} kg\n"
            f"Altura: {self.altura:g} m\n"
            f"IMC: {self.calcular_imc():.2f}\n"
            f"Situação: {self.classificar_imc()}"
        )
