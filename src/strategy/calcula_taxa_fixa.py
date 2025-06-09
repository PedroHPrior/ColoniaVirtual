# src/strategy/calcula_taxa_fixa.py

from .metodo_calculo_taxa import MetodoCalculoTaxa

class CalculaTaxaFixa(MetodoCalculoTaxa):
    """
    Implementa uma estratégia de cálculo de taxa fixa.
    """
    def __init__(self, taxa_fixa: float):
        self.taxa_fixa = taxa_fixa

    def calcular_taxa(self, valor_base: float) -> float:
        """
        Retorna uma taxa fixa, independentemente do valor_base.

        Args:
            valor_base (float): O valor sobre o qual a taxa seria calculada (ignorado nesta estratégia).

        Returns:
            float: O valor da taxa fixa.
        """
        print(f"Calculando taxa fixa: {self.taxa_fixa:.2f}")
        return self.taxa_fixa