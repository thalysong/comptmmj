import re

# Expressão regular para os diferentes tipos de índices
regex = re.compile(r"""
    (                               # Grupo para os diferentes tipos de índices
        \-?\d+                      # Inteiro positivo ou negativo, ou zero
        |
        ['"][\w\s]+['"]             # Nome de coluna entre aspas simples ou duplas
        |
        \-?\d+:\-?\d+               # Intervalo de números inteiros
        |
        ['"][\w\s]+['"]:['"][\w\s]+['"]  # Intervalo de colunas por nome entre aspas
    )
""", re.VERBOSE)

def verificar_indice(indice):
    # Retorna True se a cadeia é reconhecida como um índice válido
    return bool(regex.fullmatch(indice))

# Loop para receber entradas repetidas vezes
while True:
    # Solicita uma cadeia do usuário
    indice_usuario = input("Informe uma cadeia para verificar se é um índice válido de Pandas (ou digite 'break' para sair): ")

    # Verifica se o usuário quer sair
    if indice_usuario.lower() == "break":
        print("Encerrando o programa.")
        break

    # Verifica se a cadeia informada é um índice válido e exibe o resultado
    if verificar_indice(indice_usuario):
        print("A cadeia informada é um índice válido.")
    else:
        print("A cadeia informada NÃO é um índice válido.")
