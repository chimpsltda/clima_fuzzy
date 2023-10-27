"""Importa classe Enum para utilizar."""
from enum import Enum

class NumEscolhas(Enum):
    """Enums de perguntas disponiveis para usar"""
    VESTUARIO= "Que tipo de roupas devo usar hoje?"
    ATIVIDADES_EXTERNAS = "O Clima esta bom para eu realizar alguma atividade ao ar livre?"
    PREVISAO_CHUVA = "Devo levar um guarda-chuva?"
    AVALIACAO_DE_CONFORTO = "Como ficar confortavel em casa?"
    EFICIENCIA_ENERGETICA = "Como esta o clima para eu sair?"
    SEGURANCA_VIARIA = "Como está o clima para realizar atividades agricolas?"
    ATIVIDADES_AGRICOLAS = "O que posso usar para tornar o clima mais agradavel?"

    def values(self):
        """pega lista de todos os valores de cada valor"""
        return [self.VESTUARIO.value, self.ATIVIDADES_EXTERNAS.value,
                self.PREVISAO_CHUVA.value, self.AVALIACAO_DE_CONFORTO.value,
                self.EFICIENCIA_ENERGETICA.value, self.SEGURANCA_VIARIA.value,
                self.ATIVIDADES_AGRICOLAS.value]
