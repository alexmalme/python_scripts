import re


def find_words(word):
    """Função para filtrar por apenas letras dentro de iteráveis
    Retornará todas as letras dentro do input 'word'
    Se não encontrar nenhuma letra, retornará ''(vazio)."""
    word = str(word)
    w = "".join([char
                 if char.isalpha()
                 else ""
                 for char in word
                 ])
    return w.strip()


def find_word(word):
    """Função para encontrar palavras dentro de iteráveis,
    parando a busca ao encontrar vírgulas, pontos ou espaços
    Retornará apenas a primeira palavra encontrada
    Esta função retornará str com os valores encontrados ou ''(vazio) caso
    não encontre nada."""
    w = re.compile(r'(\w+)').search(str(word))
    return w.group(1).strip() if w else ''
