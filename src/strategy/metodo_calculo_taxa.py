# src/strategy/metodo_calculo_taxa.py

from abc import ABC, abstractmethod

class MetodoCalculoTaxa(ABC):
    """
    Classe abstrata que define a interface para os métodos de cálculo de taxa.
    Todas as estratégias de cálculo de taxa devem implementar este método.
    """
    @abstractmethod
    def calcular_taxa(self, valor_base: float) -> float:
        """
        Calcula a taxa com base em um valor base.

        Args:
            valor_base (float): O valor sobre o qual a taxa será calculada.

        Returns:
            float: O valor da taxa calculada.
        """
        pass