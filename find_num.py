import re

def find_num(num):
    """Função para encontrar algarismos de 0-9 dentro de iteráveis
    Retornará apenas aa primeira sequência de números encontrados
    Esta função não procura por '.'(pontos) podendo alterar os valores
    de floats ou números maiores que 999 (1.000)
    Esta função retornará float dos valores encontrados ou 0(zero) caso
    não encontre nenhum número."""
    rex = re.compile(r'(\d+)').search(str(num))
    if rex:
        return float(rex.group(1))
    else:
        return 0

def find_num_all(num):
    """Função para encontrar algorismos de 0-9 dentro de iteráveis
    Ela continua sua busca mesmo que encontre letras
    Não procura por '.'(pontos), podendo alterar os valores de floats
    ou números maiores que 999 (1.000)
    Esta função retorna integers. Se não encontrar nenhum número, retornará 0."""
    rex = re.compile(r'([0-9])').findall(str(num))
    if rex:
        return int("".join([*rex]))
    else:
        return 0

def find_num_(num):
    """Função para encontrar números dentro de iteráveis
    Ela também funciona para floats
    Retornará uma string somente com números
    Se não encontrar nenhum número, retornará 0"""
    num = str(num)
    n = "".join([char
                 if (
                     char.isnumeric()
                           or char == '.'
                           and num[index-1].isnumeric()
                           and num[index+1].isnumeric()
                           )
                 else ""
                 for index, char in enumerate(num)
                 ])
    return n if n != "" else 0