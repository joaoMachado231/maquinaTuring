import ply.lex as lex

# Lista de palavras-chave
palavras_chave = {
    'if': 'IF',
    'for': 'FOR',
    'while': 'WHILE',
}

# Lista de tokens
tokens = list(palavras_chave.values()) + [
    'IDENTIFICADOR',
]

# Regras para tokens simples
t_IF = r'if'
t_FOR = r'for'
t_WHILE = r'while'

# Regra para identificadores (nomes de variáveis)
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavras_chave.get(t.value, 'IDENTIFICADOR')
    return t

# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t\n'

# Função para tratar erros
def t_error(t):
    print(f"Caractere não reconhecido: '{t.value[0]}'")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()

# Exemplo de uso
codigo = """
if x > 0:
    for i in range(10):
        while y < 5:
            print("Loop!")
"""

lexer.input(codigo)

while True:
    token = lexer.token()
    if not token:
        break
    print(f'Tipo: {token.type}, Valor: {token.value}')
