import re


def find_words(word):
    """Função para filtrar por apenas letras dentro de iteráveis
    Retornará todas as letras dentro do input 'word'
    Se não encontrar nenhuma letra, retornará ''(vazio)."""
    w = ''
    for index, char  in enumerate(str(word)):
        if char.isalpha():
            w += char
    return w.strip()


def find_word(word):
    """Função para encontrar palavras dentro de iteráveis,
    parando a busca ao encontrar vírgulas, pontos ou espaços
    Retornará apenas a primeira palavra encontrada
    Esta função retornará str com os valores encontrados ou ''(vazio) caso
    não encontre nada."""
    w = re.compile(r'(\w+)').search(str(word))
    if w:
        return w.group(1)
    else:
        return ''
