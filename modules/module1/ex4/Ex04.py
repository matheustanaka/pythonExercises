import sys
from calendar import monthrange
from datetime import date


def duracao_meses():
    meses_em_dias = {}
    meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', \
            'Setembro', 'Outubro', 'Novembro', 'Dezembro'

    ano_atual = date.today().year

    for cod_mes, mes in enumerate(meses):
        meses_em_dias[mes] = monthrange(ano_atual, cod_mes + 1)[1]

    return meses_em_dias
print(duracao_meses())

sys.modules[__name__] = duracao_meses