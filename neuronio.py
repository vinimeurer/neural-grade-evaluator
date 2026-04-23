from dataclasses import dataclass


@dataclass
class NeuronioAvaliador:
    """
    Neurônio artificial para cálculo da nota bimestral.

    Cada peso representa a importância relativa de cada avaliação
    na decisão final.
    """

    peso_trabalho: float
    peso_resumo: float
    peso_prova: float
    bias: float = 0.0

    def calcular_nota(self, nota_trabalho: float, nota_resumo: float, nota_prova: float) -> float:
        """
        Calcula a nota bimestral a partir das notas individuais.

        Args:
            nota_trabalho (float): Nota do trabalho (0 a 10)
            nota_resumo (float): Nota do resumo (0 a 10)
            nota_prova (float): Nota da prova (0 a 10)

        Returns:
            float: Nota bimestral final (0 a 10)
        """

        soma_ponderada = (
            self.peso_trabalho * nota_trabalho +
            self.peso_resumo * nota_resumo +
            self.peso_prova * nota_prova +
            self.bias
        )

        # Função de ativação identidade + cláusula de segurança
        return max(0.0, min(10.0, soma_ponderada))
    
    