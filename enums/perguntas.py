from enum import Enum

class NumEscolhas(Enum):
    VESTUARIO= "Que tipo de roupas devo usar hoje?"
    ATIVIDADES_EXTERNAS = "O Clima esta bom para eu realizar alguma atividade ao ar livre?"
    PREVISAO_CHUVA = "Devo levar um guarda-chuva?"
    AVALIACAO_DE_CONFORTO = "A refrigeração interna, deve ser como?"
    EFICIENCIA_ENERGETICA = "Como esta o clima para eu sair?"
    SEGURANCA_VIARIA = "Como está o clima para realizar atividades agricolas?"
    ATIVIDADES_AGRICOLAS = "O que posso usar para tornar o clima mais agradavel?"
    
    def values():
        return [NumEscolhas.VESTUARIO.value, NumEscolhas.ATIVIDADES_EXTERNAS.value, 
                NumEscolhas.PREVISAO_CHUVA.value, NumEscolhas.AVALIACAO_DE_CONFORTO.value, 
                NumEscolhas.EFICIENCIA_ENERGETICA.value, NumEscolhas.SEGURANCA_VIARIA.value, 
                NumEscolhas.ATIVIDADES_AGRICOLAS.value]