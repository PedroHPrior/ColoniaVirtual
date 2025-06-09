# src/strategy/calcula_taxa_express.py

from .metodo_calculo_taxa import MetodoCalculoTaxa

class CalculaTaxaExpress(MetodoCalculoTaxa):
    """
    Implementa uma estratégia de cálculo de taxa para entrega expressa (porcentagem sobre o valor base).
    """
    def __init__(self, percentual_taxa: float):
        self.percentual_taxa = percentual_taxa # Ex: 0.10 para 10%

    def calcular_taxa(self, valor_base: float) -> float:
        """
        Calcula a taxa como uma porcentagem do valor base.

        Args:
            valor_base (float): O valor sobre o qual a taxa será calculada.

        Returns:
            float: O valor da taxa calculada.
        """
        taxa = valor_base * self.percentual_taxa
        print(f"Calculando taxa express ({self.percentual_taxa*100:.0f}%): {taxa:.2f}")
        return taxa