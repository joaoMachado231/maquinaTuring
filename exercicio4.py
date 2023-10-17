import re

# Expressão regular: 1*(00)*1*
padrao = r'^1*(00)*1*$'

def verifica_expressao_regular(string):
    if re.match(padrao, string):
        return True
    else:
        return False

# Exemplo de uso:
strings = ["1111", "1001", "0011", "1100111", "010101"]
for s in strings:
    if verifica_expressao_regular(s):
        print(f'A string "{s}" corresponde à expressão regular')
    else:
        print(f'A string "{s}" não corresponde à expressão regular')
