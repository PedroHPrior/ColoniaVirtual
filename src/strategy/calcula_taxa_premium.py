# src/strategy/calcula_taxa_premium.py

from .metodo_calculo_taxa import MetodoCalculoTaxa

class CalculaTaxaPremium(MetodoCalculoTaxa):
    """
    Implementa uma estratégia de cálculo de taxa premium.
    Pode ser uma combinação de taxa fixa e porcentagem, ou outra lógica complexa.
    Para este exemplo, vamos usar uma taxa fixa com um adicional por cada R$100 de valor base.
    """
    def __init__(self, taxa_minima: float, valor_por_cem: float):
        self.taxa_minima = taxa_minima
        self.valor_por_cem = valor_por_cem # Adicional para cada R$100 do valor base

    def calcular_taxa(self, valor_base: float) -> float:
        """
        Calcula a taxa premium: taxa mínima + adicional baseado no valor base.

        Args:
            valor_base (float): O valor sobre o qual a taxa será calculada.

        Returns:
            float: O valor da taxa calculada.
        """
        adicional = (valor_base // 100) * self.valor_por_cem
        taxa = self.taxa_minima + adicional
        print(f"Calculando taxa premium (min: {self.taxa_minima:.2f}, adic/100: {self.valor_por_cem:.2f}): {taxa:.2f}")
        return taxa